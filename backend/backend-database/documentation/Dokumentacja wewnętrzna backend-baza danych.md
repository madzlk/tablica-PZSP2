# Korzystanie z Fast API
fast api ma dwie metody GET:
Obie hostowane na 127.0.0.1:8000
### "/stops/"
Zwraca listę aktywnych przystanków (wraz z danymi)
### "/times/stopid/n"
Zwraca n następnych przyjazdów dla przystanku o podanym id

# Odpalenie Fast API oraz systemu bazy danych
Korzystamy z Pythona 3.6 - żeby działał z uvicornem, na którym stawiane jest FastAPI
## Utworzenie bazy danych:
**Za pierwszym razem** należy odpalić skrypt
```python3 setup_db.py```
tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

## Zapełnienie bazy danych:
Po stworzeniu bazy danych, co dzieje się raz, pierwszym programem który odpalamy jest
```python3 main.py```
będzie on w nieskończonej pętli pobierał nowe dane z API co minute, i jeżeli dane się zmienią 
(względem tych zapisanych w bazie) to je podmieni.

## Postawienie Fast API:
Fast api stawiamy przy pomocy uvicorna, bo jest prosto.
```uvicorn api_declaration:fast_api```
powinniśmy dostać w terminalu wiadomość że wszystko jest cacy, i na 127.0.0.1:8000 mamy dostępne nasze call'e.

## Sytuacje błędne:
Kiedy coś nie działa będziemy wiedzieli ponieważ w fastapi jest info kiedy zostałe pobrane dane.
Dane na temat przystanków są updatowane kiedy ktoś użyje konsoli admina ponieważ przystanki zmieniają się rzadko
i są ustawiane przez administratora.
Rozkłady jazdy sa lookup'owne co minute (około), więc jeżeli jakiś rozkład jazdy jest starszy niż ~2 minuty to wiemy że coś może być nie ok.
w rzeczywistości rozkłady jazdy zmieniają się prawdopodobnie raz na pare tygodni max, więc nawet gdyby były problemy z api miasta warszawy to nie powinno być problemu - ale informacja że dane są "stare" jest dostępna.