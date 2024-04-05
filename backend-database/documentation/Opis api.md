
1.Pobranie listy wszystkich przystanków
Opis:
Zwraca ~8200 przystanków i ich info, można założyć że to wszystkie przystanki w bazie danych API.
Przydatne do sprawdzenia czy jakiś przystanek znajduje się w bazie danych. "nazwa_zespolu" oznacza nazwę przystanka,
jeżeli jakaś nazwa znajduje się w odpowiedzi od tego request'a, to oznacza że można ją wykorzystać do wywołania innych URL.

URL:
https://api.um.warszawa.pl/api/action/dbstore_get?id=ab75c33d-3a26-4342-b36a-6e5fef0a3ac3&apikey=wartość

Parametry obowiązkowe:
&apikey={wartość klucza api}        każdy request wymaga klucza

Zwraca:
{"result":
        [{"values":
                [{"value": "1001", "key": "zespol"},
                {"value": "01", "key": "slupek"},
                {"value": "Kijowska", "key": "nazwa_zespolu"},
                {"value": "2201", "key": "id_ulicy"},
                {"value": "52.248455", "key": "szer_geo"},
                {"value": "21.044827", "key": "dlug_geo"},
                {"value": "al.Zieleniecka", "key": "kierunek"},
                {"value": "2023-12-10 00:00:00.0", "key": "obowiazuje_od"}]
            },
        {"values":
                ...
            },
        ...
        ]
}


2.Pobranie przystanków: (Bezużyteczne?)
Opis:
Szczerze mówiąc nie mam pojęcia do czego służy ta cześć API? możemy uzyskać "ID" przystanku jeżeli znamy jego nazwę,
ale nazwy nie zawsze są oczywiste, a do sprawdzenia jakie linie znajdują się na przystanku i tak potrzebujemy jeszcze numeru słupka.

URL:
https://api.um.warszawa.pl/api/action/dbtimetable_get?id=b27f4c17-5c50-4a5b-89dd-236b282bc499&name=nazwaprzystanku&apikey=wartość

Parametry obowiązkowe:
&apikey={wartość klucza api}        każdy request wymaga klucza
&name={nazwa przystanku}            request bez nazwy przystanku zwraca błąd.

Zwraca:
{"result":
        [{"values":
                [{"value": "1001", "key": "zespol"},
                {"value": "Kijowska", "key": "nazwa"}]
            }]
    }

3.Pobranie lini na przystanku:
Opis:
Na podstawie id i numeru słupka przystanku zwraca jakie linie aktualnie tam kursują. zarówno id jak i numer słupka są obowiązkowe.

URL:
https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId=wartość&busstopNr=wartość&apikey=wartość

Parametry obowiązkowe:
&apikey={wartośc klucza api}        każdy request wymaga klucza
&busstopId={numer ID przystanku}    można go dostać z 1 lub 2 URL api.
&busstopNr={numer słupka}           rozróżnia przystanki o tej samej nazwie/blisko siebie. dostajemy jako zwrot w 1 URL api.

Zwraca:
{"result":
        [{"values":
                [{"value": "102", "key": "linia"}]
            },
        {"values":
                [{"value": "123", "key": "linia"}]
            }, 
         ...
    ]
}

4.Pobranie rozkładu dla linii:
https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e60518c9f3238&busstopId=wartość&busstopNr=wartość&line=wartość&apikey=wartość
