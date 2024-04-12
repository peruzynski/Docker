Dokumentacja projektu w ramach zajęć Inżynierii Oprogramowania


I. Wymagane dokumenty
Charakterystyka oprogramowania

a. Nazwa skrócona: DockerPyApp
b. Nazwa pełna: Dockerized Python Application
c. Krótki opis ze wskazaniem celów: Dockerized Python Application jest to aplikacja napisana w języku Python, która została skonfigurowana do uruchamiania w kontenerach Docker. Celem projektu jest stworzenie przenośnej i łatwej w zarządzaniu aplikacji, która może być szybko wdrożona w różnych środowiskach. Aplikacja umożliwia użytkownikom wyszukiwanie utworów na platformie Spotify za pomocą wprowadzonego zapytania. Celem jest zapewnienie łatwego i szybkiego dostępu do ulubionych utworów oraz odkrywanie nowej muzyki.… 

Prawa autorskie
a. Autorzy: Grupa projektowa składająca się z: [Andrzej Tyszko, Bartłomiej Perużyński, Marcin Plath]
b. Warunki licencyjne do oprogramowania wytworzonego przez grupę: Oprogramowanie jest objęte licencją open source zgodnie z zasadami MIT License.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                              Specyfikacja wymagań Docerized Spotify 9000                                                                                              |
+=====+=========================================+===================================================================================================================================================+================+==================+
| Id. |                  Nazwa                  |                                                                        Opis                                                                       |    Priorytet   |     Kategoria    |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 1.  | Wyszukiwanie utworów                    | Użytkownik może wprowadzić zapytanie dotyczące utworu, który chce znaleźć na Spotify.                                                             | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 2.  | Obsługa błędów                          | System powinien obsługiwać błędy związane z brakiem zapytania, błędnym zapytaniem lub błędem w komunikacji z API Spotify.                         | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 3.  | Interfejs graficzny                     | Aplikacja powinna posiadać prosty i intuicyjny interfejs umożliwiający użytkownikowi łatwe korzystanie z funkcjonalności wyszukiwania utworów.    | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 4.  | Autoryzacja Spotify API                 | Aplikacja powinna korzystać z autoryzacji przy wykorzystaniu klucza dostępu do API Spotify, zapewniając bezpieczeństwo komunikacji.               | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 5.  | Działanie aplikacji w kontenerze Docker | Projekt musi być wykonany w sposób umożliwiający uruchomienie aplikacji w kontenerze Docker, zapewniając przenośność i łatwość wdrożenia.         | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 6.  | Informacje o utworach                   | Po wykonaniu zapytania, użytkownik powinien otrzymać informacje o znalezionych utworach, takie jak tytuł, wykonawca, album i link do odtworzenia. | 1 (wymagane)   | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 7.  | Obługa różnych rodzajów wyszukiwania    | Aplikacja powinna obsługiwać różne rodzaje wyszukiwań, takie jak: tytuł utworu, nazwa wykonawcy, fragment tekstu, etc.                            | 2 (przydatne)  | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 8.  | Personalizacja wyników wyszukiwania     | żytkownik powinien mieć możliwość personalizacji wyników wyszukiwania, takich jak sortowanie, filtrowanie czy dodatkowe informacje.               | 2 (przydatne)  | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 9.  | Testy jednostkowe                       | Projekt powinien zawierać testy jednostkowe, zapewniające sprawdzenie poprawności działania poszczególnych funkcjonalności.                       | 3 (opcjonalne) | Funkcjonalne     |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+
| 10.  | Responsywność                           | Interfejs aplikacji powinien być responsywny, umożliwiając korzystanie z niej na różnych urządzeniach i rozdzielczościach.                        | 2 (przydatne)  | Pozafunkcjonalne |
+-----+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------+

Architektura systemu/oprogramowania
a. Architektura rozwoju - stos technologiczny: Aplikacja napisana w języku Python z wykorzystaniem frameworka Flask do obsługi interfejsu HTTP. Całość uruchamiana w kontenerach Docker.
b. Architektura uruchomieniowa - stos technologiczny: Aplikacja będzie działać w kontenerach Docker.

Testy
a. Scenariusze testów:

b. Sprawozdanie z wykonania scenariuszy testów:
(Tutaj należy umieścić raport z przeprowadzonych testów)
