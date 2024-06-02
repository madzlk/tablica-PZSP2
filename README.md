# Tablica informacyjna
Celem projektu jest zapewnienie oprogramowania umożliwiającego wyświetlanie informacji dotyczących komunikacji miejskiej dla przystanków zlokalizowanych w okolicy WeiTI, włączając w to czasy odjazdów. Na ekranie (np. w formie monitora o proporcjach 21:9 w orientacji pionowej) zostanie wyświetlona mapka (np. z Google Maps lub OpenStreetMap) przedstawiająca budynek Wydziału oraz przystanki tramwajowe i autobusowe, takie jak Plac Politechniki 1, Plac Politechniki 2, Metro Politechnika 1, Metro Politechnika 2, itp., wraz z szacowanym czasem dotarcia na piechotę. Poniżej lub obok mapki znajdzie się lista środków transportu oraz godziny odjazdów.

# Uruchamianie

Przed uruchomieniem:
1. W folderze timetable-web/ należy umieścić plik **.env** z kluczem do API map google: `VITE_MAPS_API_KEY=klucz`
3. W folderze backend-database/src należy umieścić plik **.env** zawierający samą wartość klucza do API miasta api.um.warszawa.pl.
     - Jeżeli przy uruchomieniu docker compose up pojawiają się komunikaty 'db-refresh: Api call failed' to jest to spowodowanie właśnie brakiem tego pliku bądź błędnym kluczem/formatem pliku.

## Lokalnie
1. **Za pierwszym razem** należy odpalić skrypt
```python3 setup_db.py```
tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

2. Po stworzeniu bazy danych, co dzieje się raz, pierwszym programem który odpalamy jest
```python3 main.py```
będzie on w nieskończonej pętli pobierał nowe dane z API co minute, i jeżeli dane się zmienią
(względem tych zapisanych w bazie) to je podmieni.

3. Fast api stawiamy przy pomocy uvicorna, bo jest prosto.
```uvicorn api_declaration:fast_api```
powinniśmy dostać w terminalu wiadomość że wszystko jest cacy, i na 127.0.0.1:8000 mamy dostępne nasze call'e.

4. Frontend uruchamiamy za pomocą komendy:
```npm run dev```
W przypadku błędów należy upenwić się, że zostały zainstalowane odpowiednie pakiety

## Lokalnie-konteneryzacja
# Odpalenie skonteneryzowanego systemu

1. **Za pierwszym razem** należy odpalić skrypt
```python3 setup_db.py```
tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

2. Z poziomu folderu docker, należy wykonać komende
```docker-compose up --build```
bądź uruchomić skrypt ```cleanup.sh``

Jeżeli działanie zakońone zostanie z sukcesem frontend
dostępny będzie pod adresem http://localhost:5173/
, a backend pod adresem http://localhost:8000/

## Na docelowym sprzęcie
1. **Za pierwszym razem** należy odpalić skrypt
```python3 setup_db.py```
tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

2. `chmod +x startup.sh`

3. W folderze /etc/systemd/user trzeba umieścić plik **tablica.service**. Pod ExecStart musi być podana ścieżka do pliku **startup.sh** (tutaj zakładamy że pliki aplikacji są w katalogu domowym użytkownika tablica).

4. `sudo systemctl daemon-reload`

5. `systemctl --user enable tablica.service` włącza nowo zdefiniowaną usługę

6. `systemctl --user start tablica.service` uruchomi usługę.Powinien zostać uruchomiony docker compose a następnie firefox pod URL aplikacji.
     - Jeżeli aplikacja się nie uruchomi:
       - Logi wykonania skryptu znajdą się w tym folderze w pliku logs.txt.
       - Za pomocą komendy `systemctl --user status tablica.service` można zobaczyć co stało się z tablica.service.
       - Można spróbować uruchomić sam skrypt startup.sh i szukać przyczyn błędu.
     - Jeżeli aplikacja się uruchomi to powinna działać też przy uruchomieniu systemu, jeżeli tak nie działa to także można skorzystać z metod podanych wcześniej.

7. W pliku /etc/default/apport zmienić wartość enabled na 0 aby komunikaty o błędach systemu nie wyświetlały się nad aplikacją

8. Można zmienić screen blank na never żeby ekran się nie wygaszał.