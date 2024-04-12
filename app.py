from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SPOTIFY_API_KEY = None

# Pobieranie klucza dostępu do API Spotify
def get_spotify_api_key():
    global SPOTIFY_API_KEY
    if not SPOTIFY_API_KEY:
        url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': '3668fff8ab484f829b23705eb5ec7221',
            'client_secret': '3e1a31c9cec54cc6b671ebd5d0fcbc82'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            SPOTIFY_API_KEY = response.json()['access_token']
            print("Pomyślnie uzyskano klucz dostępu:", SPOTIFY_API_KEY)
        else:
            print("Wystąpił błąd:", response.text)


@app.route('/')
def index():
    get_spotify_api_key()  # Upewniamy się, że mamy klucz dostępu przed wyświetleniem strony
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    get_spotify_api_key()
    query = request.form['query']
    if not query:
        return render_template('index.html', error='Proszę wprowadzić zapytanie.')

    url = f'https://api.spotify.com/v1/search?q={query}&type=track'
    headers = {'Authorization': f'Bearer {SPOTIFY_API_KEY}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return render_template('index.html', error='Wystąpił błąd podczas wyszukiwania utworów.')

    data = response.json()
    tracks = data.get('tracks', {}).get('items', [])

    # Dodajemy warunek, aby sprawdzić, czy utwór ma miniaturę
    for track in tracks:
        if not track['album']['images']:
            # Jeśli brak miniatury, ustawiamy domyślny adres URL miniatury
            track['album']['images'].append({'url': 'link_do_domyślnej_miniatury.jpg'})

    return render_template('index.html', tracks=tracks)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='6969')


