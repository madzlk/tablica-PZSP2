# Odpalenie skonteneryzowanego systemu

## Konfiguracja:
W pierwzym kroku należy stworzyć plik .env w folderze backend-database
i zamieścić w nim klucz api miasta warszawy. Klucz api można wygenerować poprzez stworznie konta na stronie
https://api.um.warszawa.pl/

## Utworzenie bazy danych:
**Za pierwszym razem** należy odpalić skrypt
```python3 setup_db.py```
tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

## Stworzenie kontenerów:
Z poziomu folderu docker, należy wykonać komende
```docker-compose up --build```
Jeżeli komenda ukończy działanie z sukcesem frontend
dostępny będzie pod adresem http://localhost:5173/
, a backend pod adresem http://localhost:8000/
