### Wstęp

W tej instrukcji opisany jest sposób konfiguracji automatycznego uruchamiania tablicy przy starcie systemu, domyślnie użyta została maszyna wirtualna z systemem operacyjnym **Ubuntu 24.04**. Instrukcja zakłada że nazwa użytkownika systemu to _tablica_, w innym przypadku należy ją podmienić w dostarczonych skryptach.

### Konfiguracja

1. Do poprawnego działania aplikacji potrzebny jest **docker** oraz przeglądarka firefox.
   - Należy dodać użytkownika _tablica_ do grupy **docker** wedle instrukcji: https://docs.docker.com/engine/install/linux-postinstall/, inaczej skrypt nie będzie działać.
2. Klonujemy zdalne repozytorium do katalogu domowego.
3. W folderze timetable-web/ należy umieścić plik **.env** z kluczem do API map google: `VITE_MAPS_API_KEY=klucz`
4. W folderze backend-database/src należy umieścić plik **.env** zawierający samą wartość klucza do API miasta api.um.warszawa.pl.
   - Jeżeli przy uruchomieniu docker compose up pojawiają się komunikaty 'db-refresh: Api call failed' to jest to spowodowanie właśnie brakiem tego pliku bądź błędnym kluczem/formatem pliku.
5. Uruchomić raz skrypt **setup_db.py** (w folderze backend-database/src/)
6. `chmod +x startup.sh` (w folderze boot/)
7. W pliku **tablica.service** do wartości ExecStart należy przypisać ścieżke do pliku **startup.sh** (tutaj zakładamy że pliki aplikacji są w katalogu domowym użytkownika tablica). W folderze /etc/systemd/user trzeba umieścić plik **tablica.service**, można tego dokonać wykorzystując komende `cp`
8. `sudo systemctl daemon-reload`
9. `systemctl --user enable tablica.service` włącza nowo zdefiniowaną usługę
10. `systemctl --user start tablica.service` uruchomi usługę.Powinien zostać uruchomiony docker compose a następnie firefox pod URL aplikacji.

- Jeżeli aplikacja się nie uruchomi:
  - Logi wykonania skryptu znajdą się w tym folderze w pliku logs.txt.
  - Za pomocą komendy `systemctl --user status tablica.service` można zobaczyć co stało się z tablica.service.
  - Można spróbować uruchomić sam skrypt startup.sh i szukać przyczyn błędu.
- Jeżeli aplikacja się uruchomi to powinna działać też przy uruchomieniu systemu, jeżeli tak nie działa to także można skorzystać z metod podanych wcześniej.

**W przypadku problemów serwis można dezaktywować `systemctl --user disable tablica.service`, po restarcie systemu serwis nie będzie już aktywny**
**terminal można uruchomić za pomocą skrótu Ctrl+Alt+T**

11. **Watchdog**

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

12. W pliku /etc/default/apport zmienić wartość enabled na 0 aby komunikaty o błędach systemu nie wyświetlały się nad aplikacją
13. Można zmienić screen blank na never żeby ekran się nie wygaszał.
