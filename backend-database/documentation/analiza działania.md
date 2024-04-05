
# Funkcje:
 1. Tworzenie bazy danych + tabel
 2. Generacja odpowiednich API call'i
 3. Wykonanie API call'i
 4. Populacja bazy danych danymi z API
 5. Udostępnianie danych z bazy danych przez FastAPI

 6. Modyfikacja "konfiguracji" aplikacji - interfejs do zmiany zawartości głównej tabeli

 7. testy (?)

# Baza danych:
## Tabele:
Uzasadnienie:
Projekt nie wymaga skomplikowanej warstwy danych stałych - główną funkcją bazy danych jest przechowywanie informacji na temat stałej konfiguracji aplikacji tzn. które przystanki powinny być branę pod uwagę na mapie; ze względu na to że informacje nie będą pobierane cały czas, one również są zapisywane, wraz z oznaczeniem kiedy zostałe pobrane - w ten sposób nawet kiedy API jest niedostępne cały projekt może nadal działać, albo w trybie "potencjalnie przestarzałego rozkładu" albo w trybie "przeciętnych odstępów" (np. ten autobus jeździ co 20 minut).
### Przystanki:
Opisuje wszystkie przystanki, na podstawie tego jakie przystanki są wpisane w tej tabeli i które posiadają "1" w polu "czy brać pod uwagę na mapie" takie dane będą dostępne przez fastAPI

1. (PK) id przystanku API - połączenie (konkatenacja) "numeru zespołu" i "numeru słupka" z bazy API, id które pozawala jednoznacznie okreslić przystanek wewnątrz API
2. wewnętrzne id przystanku - id nadane wewnętrznie przez nas danemu przystankowi
3. Nazwa przystanku - nazwa przystanku według API
4. szerokość geograficzna
5. długość geograficzna
6. odległość od tablicy w minutach marszu
7. kierunek (nazwa ulicy)
8. dane pobrane (data i godzina)
9. czy brać pod uwagę na mapie

### Rozkłady_Jazdy:
Kompendium rozkładów jazdy w który znajdują się dane na temat wszystkich godzin przyjazdów autobusów i tramwajów na wszystkich przystankach

1. (PK) id wpisu rozkładu jazdy
2. (FK) id przystanku API - jak wyżej
3. linia autobusu
4. kierunek (nazwa przystanku)
5. czas przyjazdu
6. brygada - nadawana w API, może być przydatna w przypadku przewidywania potencjalnego spóźnienia autobusów, dodana do bazy tak żeby nie trzeba było jej modyfikować w razie potrzeby wprowadzenia tego rozszerzenia funkcjonalności
7. dane pobrane (data i godzina)

# Realizacja funkcji przez klasy:
## Database Handler:

## API Handler:
 - tworzy zestaw calli API na podstawie dostarczonych danych
 - wykonuje calle API
 - procesuje dane z calli API na format przystępny dla bazy danych

## FastAPI Handler:

