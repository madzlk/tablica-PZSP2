# This script should only be run once.
import sqlite3
from datetime import datetime

# Nothing to test here as well, this is just an SQLite script,
# And it should only be run once, to being the operation of the whole system.

# Create the database, connect to the database, create cursor
con = sqlite3.connect("tablica.db")
cur = con.cursor()

# Dropping Tables just in case.
cur.execute("DROP TABLE IF EXISTS przystanki")
cur.execute("DROP TABLE IF EXISTS rozkład_jazdy")

# Creating przystanki table
cur.execute("""CREATE TABLE IF NOT EXISTS przystanki (
    id                       PRIMARY KEY ON CONFLICT FAIL,
    wewnętrzne_id            INTEGER NOT NULL UNIQUE ON CONFLICT FAIL,
    nazwa                    NVARCHAR2(64) NOT NULL,
    szer_geo                 FLOAT(8) NOT NULL,
    dlug_geo                 FLOAT(8) NOT NULL,
    odległość                INTEGER,
    kierunek                 NVARCHAR2(64),
    data_ostatniego_pobrania TIMESTAMP NOT NULL,
    aktywny                  CHAR(1) NOT NULL
);""")

# Creating rozkład_jazdy table
cur.execute("""CREATE TABLE IF NOT EXISTS rozkład_jazdy (
    id_wpisu                 INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    przystanki_id            REFERENCES przystanki(ID) ON DELETE CASCADE NOT NULL,
    linia                    INTEGER NOT NULL,
    kierunek                 NVARCHAR2(64) NOT NULL,
    czas_przyjazdu           TIME NOT NULL,
    brygada                  INTEGER,
    trasa                    NVARCHAR2(32) NOT NULL,
    data_ostatniego_pobrania TIMESTAMP NOT NULL
);""")

# Inserting data into przystanki table - if at any point the stops that are visible should change, this will create problems.
# WHICH IS WHY YOU ONLY RUN THIS ONCE AFTER THE SYSTEM BEGINS WORKING.
# or you just run this again an then add the other stops via the administrator console.
now = datetime.now()
cur.execute(f"""INSERT INTO przystanki VALUES
            (700501, 1, 'pl.Politechniki', 52.220031, 21.011500, 1, 'Metro Politechnika', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700502, 2, 'pl.Politechniki', 52.220071, 21.010984, 1, 'al.Niepodległości', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700601, 3, 'Metro Politechnika', 52.216862, 21.013961, 8, 'Marszałkowska', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700602, 4, 'Metro Politechnika', 52.217260, 21.013801, 7, 'GUS', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700603, 5, 'Metro Politechnika', 52.219940, 21.014997, 5, 'pl.Zbawiciela', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700604, 6, 'Metro Politechnika', 52.219933, 21.016035, 6, 'pl.Politechniki', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700605, 7, 'Metro Politechnika', 52.218744, 21.015268, 5, 'rondo Jazdy Polskiej', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700607, 8, 'Metro Politechnika', 52.219250, 21.015343, 5, 'rondo Jazdy Polskiej', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700609, 9, 'Metro Politechnika', 52.219489, 21.015401, 5, 'rondo Jazdy Polskiej', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700610, 12, 'Metro Politechnika', 52.218539, 21.015497, 7, 'pl.Konstytucji', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '0'),
            (700612, 10, 'Metro Politechnika', 52.218778, 21.015517, 7, 'pl.Konstytucji', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700614, 11, 'Metro Politechnika', 52.219201, 21.015599, 7, 'pl.Konstytucji', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '1'),
            (700651, 13, 'Metro Politechnika', 52.217019, 21.014412, 8, 'null', strftime("%Y-%m-%d %H:%M:%f", "{now}"), '0')
""")
con.commit()
cur.close()
con.close()