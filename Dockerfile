# Wybierz obraz bazowy
FROM python:latest

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki aplikacji do kontenera
COPY . .

# Zainstaluj zależności
RUN pip install -r requirements.txt

# Uruchom aplikację w kontenerze
CMD ["python", "app.py"]
