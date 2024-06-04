# Tablica odjazdów

![image](https://github.com/madzlk/tablica-PZSP2/assets/70140679/7b932f9c-8778-473e-9847-4e532dad168a)

Celem projektu jest zapewnienie oprogramowania umożliwiającego wyświetlanie informacji dotyczących komunikacji miejskiej dla przystanków zlokalizowanych w okolicy WeiTI, włączając w to czasy odjazdów. Na ekranie (np. w formie monitora o proporcjach 21:9 w orientacji pionowej) zostanie wyświetlona mapka (np. z Google Maps lub OpenStreetMap) przedstawiająca budynek Wydziału oraz przystanki tramwajowe i autobusowe, takie jak Plac Politechniki 1, Plac Politechniki 2, Metro Politechnika 1, Metro Politechnika 2, itp., wraz z szacowanym czasem dotarcia na piechotę. Poniżej lub obok mapki znajdzie się lista środków transportu oraz godziny odjazdów.

# Uruchamianie

Przed uruchomieniem:

1. W folderze timetable-web/ należy utworzyć plik **.env**, a w nim umieścić linijke: `VITE_MAPS_API_KEY=klucz`, klucz należy wygenerować przez (https://developers.google.com/maps/third-party-platforms/wordpress/generate-api-key?hl=pl)[GoogleMapsPlatform].
2. W folderze backend-database/src należy utworzyć plik **.env** zawierający samą wartość klucza do (https://api.um.warszawa.pl./)[APImiasta]; klucz zostanie udostępniony po założeniu konta.

## Lokalnie

1. Stwórz wirtualne środowisko za pomocą komendy `python -m venv tablica`,
   następnie uruchom wirtualne środowisko przez komendy:

- Windows: `.\tablica\Scripts\activate`
- Linux/MacOS: `source tablica/bin/activate`

2. Instalujemy pakiety z pliku /backend-database/src/requirements.txt,
   za pomocą komendy `pip install -r requirements.txt`

3. **Za pierwszym razem** należy odpalić skrypt
   `python3 setup_db.py`
   tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
   w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

4. Po stworzeniu bazy danych, co dzieje się raz, pierwszym programem który odpalamy jest
   `python3 main.py`
   będzie on w nieskończonej pętli pobierał nowe dane z API co minute, i jeżeli dane się zmienią
   (względem tych zapisanych w bazie) to je podmieni.

5. W kolejnym terminalu (pamiętaj o aktywowaniu wirtualnego środowisko pkt.1) stawiamy Fast api przy pomocy uvicorna, bo jest prosto.
   `uvicorn api_declaration:fast_api`
   powinniśmy dostać w terminalu wiadomość że wszystko jest cacy, i na 127.0.0.1:8000 mamy dostępne nasze call'e.

6. Kolejny terminal posłuży do uruchomienia frontendu.

   Przed rozruchem, musimy dokonać małych zmian w konfiguracji.
   W pliku `tablica-PZSP2/timetable-web/vite.config.ts`, należy podmienić  
   wartość klucza target na `http://127.0.0.1:8000`, zgodnie z komentarzami.

   Zaczynamy od instalacji modułów `npm install` (założono instalacje Node JS we własnym zakresie),
   a następnie uruchmiamy frontend za pomocą `npm run dev`
   W przypadku błędów należy upenwić się, że zostały zainstalowane odpowiednie pakiety

Po wykonaniu powyższych korków frontend
dostępny będzie pod adresem http://localhost:5173/,a backend pod adresem http://localhost:8000/

## Lokalnie-konteneryzacja

# Odpalenie skonteneryzowanego systemu

1. **Za pierwszym razem** należy odpalić skrypt
   `python3 setup_db.py`
   tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
   w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

Jeżeli setup_db.py odpalimy jeszcze raz, wymarzemy zawartość wszystkich tabel w bazie.

2. Z poziomu folderu docker, należy wykonać komende
   `docker-compose up --build` (założono instalacje Docker/Docker Compose we własnym zakresie)
   bądź uruchomić skrypt ``cleanup.sh`

Jeżeli działanie zakońone zostanie z sukcesem frontend
dostępny będzie pod adresem http://localhost:5173/
, a backend pod adresem http://localhost:8000/

## Na docelowym sprzęcie

### Konfiguracja automatycznego uruchamiania

W instrukcji opisany jest sposób konfiguracji automatycznego uruchamiania tablicy przy starcie systemu i systemu watchdog (ubuntu 24.04). Instrukcja zakłada że nazwa użytkownika systemu to _tablica_, w innym przypadku należy ją podmienić w dostarczonych skryptach. Jednak gorąco zalecane jest stworzenie nowego użytkwonika o zadanej nazwie.

1. Do poprawnego działania aplikacji potrzebny jest **docker** oraz przeglądarka firefox.

   - Należy dodać użytkownika _tablica_ do grupy **docker** wedle instrukcji: https://docs.docker.com/engine/install/linux-postinstall/, inaczej skrypt nie będzie działać.

2. Klonujemy zdalne repozytorium do katalogu domowego.

3. W folderze timetable-web/ należy utworzyć plik **.env**, a w nim umieścić linijke: `VITE_MAPS_API_KEY=klucz`, klucz należy wygenerować przez (https://developers.google.com/maps/third-party-platforms/wordpress/generate-api-key?hl=pl)[GoogleMapsPlatform].

4. W folderze backend-database/src należy utworzyć plik **.env** zawierający samą wartość klucza do (https://api.um.warszawa.pl./)[APImiasta]; klucz zostanie udostępniony po założeniu konta.

5. **Za pierwszym razem** należy odpalić skrypt
   `python3 setup_db.py` (w folderze backend-database/src/)
   tworzy strukturę bazy danych i zapisuje ją w pliku 'tablica.db';
   w tym pliku będą notowane wszystkie ewentualne zmiany w bazie danych.

6. `chmod +x startup.sh`(w folderze boot/)

7. W pliku **tablica.service** do wartości ExecStart należy przypisać ścieżke do pliku **startup.sh** (tutaj zakładamy że pliki aplikacji są w katalogu domowym użytkownika tablica). W folderze /etc/systemd/user trzeba umieścić plik **tablica.service**, można tego dokonać wykorzystując komende `cp`

8. `sudo systemctl daemon-reload`

9. `systemctl --user enable tablica.service` włącza nowo zdefiniowaną usługę

10. `systemctl --user start tablica.service` uruchomi usługę.Powinien zostać uruchomiony docker compose a następnie firefox pod URL aplikacji.

- Jeżeli aplikacja się nie uruchomi:
  - Logi wykonania skryptu znajdą się w tym folderze w pliku logs.txt.
  - Za pomocą komendy `systemctl --user status tablica.service` można zobaczyć co stało się z tablica.service.
  - Można spróbować uruchomić sam skrypt startup.sh i szukać przyczyn błędu.
- Jeżeli aplikacja się uruchomi to powinna działać też przy uruchomieniu systemu, jeżeli tak nie działa to także można skorzystać z metod podanych wcześniej.

**W przypadku problemów serwis można dezaktywować `systemctl --user disable tablica.service`, po restarcie maszyny serwis nie będzie już aktywny**
**terminal można uruchomić za pomocą skrótu Ctrl+Alt+T**

11. W pliku /etc/default/apport zmienić wartość enabled na 0 aby komunikaty o błędach systemu nie wyświetlały się nad aplikacją
12. Można zmienić screen blank na never żeby ekran się nie wygaszał.

### Konfiguracja automatycznego restaru (moduł watchdog)

1. `sudo apt install watchdog`
2. `sudo modprobe softdog`
3. `sudo nano /etc/default/watchdog` i ustawić w pliku takie opcje:
   ```
   # Start watchdog at boot time? 0 or 1
   run_watchdog=1
   # Load module before starting watchdog
   watchdog_module="softdog"
   # Specify additional watchdog options here (see manpage).
   watchdog_options="-b"
   ```
4. `sudo nano /etc/watchdog.conf` i upewnić się że tak wyglądają jedyne niezakomentowane linijki:
   ```
   watchdog-device = /dev/watchdog
   realtime = yes
   priority = 1
   ```
5. Po `sudo service watchdog stop` i `sudo service watchdog start` watchdog powinien już działać
6. **Uwaga: ta komenda zrestartuje system -** Jeżeli wpiszemy `sudo kill -STOP $(cat /var/run/watchdog.pid)`, zakłóci to prace watchdoga i po 60 sekundach nastąpi restart systemu, co udowodni że watchdog działa.
