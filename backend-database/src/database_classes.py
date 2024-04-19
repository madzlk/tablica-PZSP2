import sqlite3
from datetime import datetime

#===============================================DATABASE OBSERVER==============================================
# This Class monitors for changes in the database using a hash,
# and when a new state of the database is detected, it sends the signal to all of it's subscribers via
# the "Update data" method, all subscribers need to have this method implemented.
class DatabaseObserver:
    def __init__(self, database_facade):
        self.subscribers = []
        self.database_facade = database_facade
        self.database_state = self.prepare_database_hash()

# Creates a hash from the database to use for comparison 
# ignores unnecessary fields such as ids or timestamps (which get updated every time the database is updated)
    def prepare_database_hash(self):
        stops = str(self.database_facade.get_stops_hash())
        timetables = str(self.database_facade.get_timetables_hash())
        database = stops + timetables
        db_hash = hash(database)
        return db_hash
    
    def add_subscriber(self, sub):
        self.subscribers.append(sub)

# If the state has changed, change internal state to new state and return True (to signal change)
    def check_for_change(self):
        new_hash = self.prepare_database_hash()
        if new_hash != self.database_state:
            self.database_state = new_hash
            return True
        return False
    
# Check for changes and if changes have occured, send new database state to subscribers
    def update(self):
        if self.check_for_change():
            for sub in self.subscribers:
                sub.update_data()

#===========================================DATABASE ADAPATER===========================================
# Makes the data from the database facade more comfortable to work with
class DatabaseAdapter:
    def __init__(self) -> None:
        pass

# turns the result of a query into a list
    def parse_database_stop_ids(self, stops):
        n_stops = []
        for stop in stops:
            n_stops.append(stop[0])
        return n_stops
    
# turns the dict used for easy access to data into a form that can be put into INSERT queries
    def turn_timetables_into_query(self, timetables):
        now = datetime.now()
        result = []
        for stop in timetables:
            for line in timetables[stop]:
                for time in timetables[stop][line]:
                    result.append((stop, line, time[1], time[3], time[0], time[2], str(now)))
        return result

#======================================DATABASE FACADE===============================================
# This Class acts as a simple interface with the internal database
class DatabaseFacade:
    def __init__(self, database_adapter, database_file):
        self.data_adp = database_adapter
        self.db_file = database_file

# Function used to get results of a query, with proper cursor management.
    def fetchall_query(self, query, values):
        con = sqlite3.connect(self.db_file)
        cur = self.con.cursor()
        result = cur.execute(query)
        ret = result.fetchall()
        con.commit()
        cur.close()
        con.close()
        return ret

# Function used to execute a command and commit it to the database, with proper cursor management.
    def execute_and_commit(self, query, values):
        con = sqlite3.connect(self.db_file)
        cur = self.con.cursor()
        cur.execute(query, values)
        self.connection.commit()
        cur.close()
        con.close()

# returns the contents of przystanki table
    def get_stops(self):
        return self.fetchall_query('SELECT * FROM przystanki', ())
        
# returns the contents of rozkład_jazdy table
    def get_timetables(self):
        return self.fetchall_query('SELECT * FROM rozkład_jazdy', ())

# returns the data in przystanki table that is a relevant to a hash
    def get_stops_hash(self):
        return self.fetchall_query('SELECT id, wewnętrzne_id, nazwa, szer_geo, dlug_geo, odległość, kierunek, aktywny FROM przystanki', ())

# returns the data in rozkład table that is relevant to a hash
    def get_timetables_hash(self):
        return self.fetchall_query('SELECT przystanki_id, linia, kierunek, czas_przyjazdu, brygada, trasa FROM rozkład_jazdy', ())

# returns the ids of "active" stops (stops that have aktywny = '1')
    def get_active_stops_id(self):
        res = self.fetchall_query('SELECT * FROM przystanki WHERE aktywny = "1"', ())
        return self.data_adp.parse_database_stop_ids(res)

# Inserts new timetable data (and delete the old data)
    def set_timetables(self, new_timetables):
        self.execute_and_commit('DELETE FROM rozkład_jazdy', ())
        new_timetables_query = self.data_adp.turn_timetables_into_query(new_timetables)
        con = sqlite3.connect(self.db_file)
        cur = self.con.cursor()
        tt_1 = new_timetables_query[0]
        cur.execute(f"INSERT INTO rozkład_jazdy VALUES(1, ?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", tt_1)
        cur.executemany(f"INSERT INTO rozkład_jazdy( przystanki_id, linia, kierunek, czas_przyjazdu, brygada, trasa, data_ostatniego_pobrania) VALUES(?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", new_timetables_query[1:])
        con.commit()
        cur.close()
        con.close()

# Insert another row to the przystanki table
    def add_stop(self, stop):
        self.execute_and_commit(f'INSERT INTO przystanki VALUES(?)', (stop))

# Remove a stop by id
    def remove_stop(self, stop_id):
        self.execute_and_commit(f'DELETE FROM przystanki WHERE id = ?', (stop_id))

# Change the value of the 'Aktywny" status of a stop
    def set_active_inactive(self, stop_id, new_status):
        self.execute_and_commit(f'UPDATE przystanki SET aktywny = ? WHERE id = ?', (new_status, stop_id))
