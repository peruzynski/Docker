import unittest
from unittest.mock import patch, MagicMock
from app import app, get_spotify_api_key

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.requests.post')
    def test_get_spotify_api_key_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'access_token': 'dummy_token'}
        
        get_spotify_api_key()
        self.assertIsNotNone(app.SPOTIFY_API_KEY)
        self.assertEqual(app.SPOTIFY_API_KEY, 'dummy_token')

    @patch('app.requests.post')
    def test_get_spotify_api_key_failure(self, mock_post):
        mock_post.return_value.status_code = 400
        
        get_spotify_api_key()
        self.assertIsNone(app.SPOTIFY_API_KEY)

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.requests.get')
    def test_search_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'tracks': {
                'items': [{'name': 'dummy_track', 'album': {'images': [{'url': 'dummy_url'}]}}]
            }
        }

        response = self.app.post('/search', data={'query': 'dummy_query'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'dummy_track', response.data)
        self.assertIn(b'dummy_url', response.data)

    @patch('app.requests.get')
    def test_search_no_query(self, mock_get):
        response = self.app.post('/search', data={'query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Proszę wprowadzić zapytanie.', response.data)

    @patch('app.requests.get')
    def test_search_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        
        response = self.app.post('/search', data={'query': 'dummy_query'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wystąpił błąd podczas wyszukiwania utworów.', response.data)

if __name__ == '__main__':
    unittest.main()
