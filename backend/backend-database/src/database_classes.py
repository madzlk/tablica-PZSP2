import sqlite3
from datetime import datetime

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
                sub.update_data(self.database_facade.get_stops(), self.database_facade.get_timetables())

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

# This Class acts as a simple interface with the internal database
class DatabaseFacade:
    def __init__(self, database_adapter, database_file):
        self.data_adp = database_adapter
        self.connection = sqlite3.connect(database_file)

    # Function used to get results of a query, with proper cursor management.
    def fetchall_query(self, query, values):
        cursor = self.connection.cursor()
        result = cursor.execute(query)
        ret = result.fetchall()
        self.connection.commit()
        cursor.close()
        return ret

    # Function used to execute a command and commit it to the database, with proper cursor management.
    def execute_and_commit(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    # returns the contents of przystanki table
    def get_stops(self):
        return self.fetchall_query('SELECT * FROM przystanki', ())

    # returns the contents of rozkład_jazdy table
    def get_timetables(self):
        return self.fetchall_query('SELECT * FROM rozkład_jazdy', ())

    def get_stops_hash(self):
        return self.fetchall_query('SELECT id, wewnętrzne_id, nazwa, szer_geo, dlug_geo, odległość, kierunek, aktywny FROM przystanki', ())

    def get_timetables_hash(self):
        return self.fetchall_query('SELECT przystanki_id, linia, kierunek, czas_przyjazdu, brygada, trasa FROM rozkład_jazdy', ())

    def get_active_stops_id(self):
        return self.fetchall_query('SELECT * FROM przystanki WHERE aktywny = "1"', ())

    def set_timetables(self, new_timetables):
        self.execute_and_commit('DELETE FROM rozkład_jazdy', ())
        new_timetables_query = self.data_adp.turn_timetables_into_query(new_timetables)
        cursor = self.connection.cursor()
        tt_1 = new_timetables_query[0]
        cursor.execute(f"INSERT INTO rozkład_jazdy VALUES(1, ?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", tt_1)
        for tt in new_timetables_query[1:]:            
            cursor.execute(f"INSERT INTO rozkład_jazdy( przystanki_id, linia, kierunek, czas_przyjazdu, brygada, trasa, data_ostatniego_pobrania) VALUES(?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", tt)
        self.connection.commit()
        cursor.close()

    def add_stop(self, stop):
        self.execute_and_commit(f'INSERT INTO przystanki VALUES(?)', (stop))

    def remove_stop(self, stop_id):
        self.execute_and_commit(f'DELETE FROM przystanki WHERE id = ?', (stop_id))

    def set_active_inactive(self, stop_id, new_status):
        self.execute_and_commit(f'UPDATE przystanki SET aktywny = ? WHERE id = ?', (new_status, stop_id))
