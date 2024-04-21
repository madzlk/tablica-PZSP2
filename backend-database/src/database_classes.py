import sqlite3
from datetime import datetime

class DatabaseError(Exception):
    pass

# Functions that are deterministic (can be tested):
# DatabaseAdapter:
# - parse database stop ids
# - turn timetables into query
# - parse times
#
# DatabaseFacade:
# None, all of them use the database, mocking a database would be pointless since
# it would just be testing our mock methods, and not the interactions with an actual database

# Status of tests: All written, all passing

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
    
# turn the result of a query into a table of times starting with now and going up (and back around if necessary)
    def parse_times(self, times):
        times = list(times)
        now = datetime.strftime(datetime.now(), '%H:%M:%S')
        now_in_times = 0
        for id, time in enumerate(times):
            if time[2] >= now:
                now_in_times = id
                break
        n_times = times[now_in_times:]
        n_times.extend(times[:now_in_times])
        return n_times

#======================================DATABASE FACADE===============================================
# This Class acts as a simple interface with the internal database
class DatabaseFacade:
    def __init__(self, database_file, database_adapter):
        self.data_adp = database_adapter
        self.db_file = database_file

# Function used to get results of a query, with proper cursor management.
    def fetchall_query(self, query, values):
        try:
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            result = cur.execute(query, values)
            ret = result.fetchall()
            cur.close()
            con.close()
            return ret
        except:
            raise DatabaseError('An Error with the database has occured')

# Function used to execute a command and commit it to the database, with proper cursor management.
    def execute_and_commit(self, query, values):
        try:
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            cur.execute(query, values)
            con.commit()
            cur.close()
            con.close()
        except:
            raise DatabaseError('An Error with the database has occured')

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
    def get_active_stops_ids(self):
        res = self.fetchall_query('SELECT * FROM przystanki WHERE aktywny = "1"', ())
        return self.data_adp.parse_database_stop_ids(res)
    
# returns the ids of "active" stops (stops that have aktywny = '1')
    def get_active_stops(self):
        res = self.fetchall_query('SELECT * FROM przystanki WHERE aktywny = "1"', ())
        return res

# returns n next buses/trams that will arrive at stop with given id
    def get_n_next_times(self, stop_id, n):
        res = self.data_adp.parse_times(self.fetchall_query('SELECT linia, kierunek, czas_przyjazdu, brygada, trasa, data_ostatniego_pobrania FROM rozkład_jazdy WHERE przystanki_id = ? ORDER BY czas_przyjazdu', (stop_id,)))
        return res[:n]

# Inserts new timetable data (and delete the old data)
    def update_data(self, new_timetables):
        try:
            self.execute_and_commit('DELETE FROM rozkład_jazdy', ())
            new_timetables_query = self.data_adp.turn_timetables_into_query(new_timetables)
            con = sqlite3.connect(self.db_file)
            cur = con.cursor()
            tt_1 = new_timetables_query[0]
            cur.execute(f"INSERT INTO rozkład_jazdy VALUES(1, ?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", tt_1)
            cur.executemany(f"INSERT INTO rozkład_jazdy( przystanki_id, linia, kierunek, czas_przyjazdu, brygada, trasa, data_ostatniego_pobrania) VALUES(?, ?, ?, ?, ?, ?, strftime('%Y-%m-%d %H:%M:%f', ?))", new_timetables_query[1:])
            con.commit()
            cur.close()
            con.close()
        except:
            raise DatabaseError('An Error with the database has occured')

# Changes only the times in every entry to rozkład_jazdy, this method is used
# when the data from the API has been checked and it's the same that it was before.
    def update_time(self):
        self.execute_and_commit("UPDATE rozkład_jazdy SET data_ostatniego_pobrania = strftime('%Y-%m-%d %H:%M:%f', ?)", (str(datetime.now()),))

# Insert another row to the przystanki table
    def add_stop(self, stop):
        self.execute_and_commit(f'INSERT INTO przystanki VALUES(?)', (stop))

# Remove a stop by id
    def remove_stop(self, stop_id):
        self.execute_and_commit(f'DELETE FROM przystanki WHERE id = ?', (stop_id))

# Change the value of the 'Aktywny" status of a stop
    def set_active_inactive(self, stop_id, new_status):
        self.execute_and_commit(f'UPDATE przystanki SET aktywny = ? WHERE id = ?', (new_status, stop_id))
