import requests
from datetime import datetime, timedelta

class CouldNotConnect(Warning):
    pass

class IncorrectApiCall(Warning):
    pass

# Functions that are deterministic (can be tested):
# Data Observer:
# - prepare hash
# - check for change
# 
# Api Facade:
# Similar to database facade, none, since we would be testing our mocked functions and not the actual connection to the api
#
# Api Adapter:
# - parse api stops
# - parse api lines
# - parse api timetables
# - fix time

# Status of tests: Not written, not passing

#===============================================DATABASE OBSERVER==============================================
# This Class monitors for changes in the data using a hash,
# and when a new state of the data is detected, it sends the signal to all of it's subscribers via
# the "Update data" method, all subscribers need to have this method implemented.
class DataObserver:
    def __init__(self):
        self.subscribers = []
        self.data_hash = 0

# Creates a hash from the data to use for comparison 
# ignores unnecessary fields such as ids or timestamps (which get updated every time the data is updated)
    def prepare_hash(self, data):
        data_hash = hash(str(data))
        return data_hash
    
    def add_subscriber(self, sub):
        self.subscribers.append(sub)

# If the state has changed, change internal state to new state and return True (to signal change)
    def check_for_change(self, data):
        new_hash = self.prepare_hash(data)
        if new_hash != self.data_hash:
            self.data_hash = new_hash
            return True
        return False
    
# Check for changes and if changes have occured, send new data state to subscribers,
# otherwise sends the signal to update the time (since the data hasn't changed, but it has been checked.)
    def update(self, data):
        if self.check_for_change(data):
            for sub in self.subscribers:
                sub.update_data(data)
        else:
            for sub in self.subscribers:
                sub.update_time()

#============================================API FACADE======================================================
# Provides a convenient interface for working with the API
class ApiFacade:
    def __init__(self, api_key, api_adapter):
        self.api_key = api_key
        self.api_adapter = api_adapter

# Returns the list of all stops with their data (there's around 8000)
    def get_all_stops(self):
        try:
            response = (requests.get(f'https://api.um.warszawa.pl/api/action/dbstore_get?id=ab75c33d-3a26-4342-b36a-6e5fef0a3ac3&apikey={self.api_key}').json())
            return self.api_adapter.parse_api_stops(response)
        except:
            raise CouldNotConnect("Couldn't connect to the API")

# Returns lines that are available at a given stop
    def get_lines_for_stop(self, stop_id):
        try:
            response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId={int(stop_id/100)}&busstopNr={str(stop_id)[-2:]}&apikey={self.api_key}').json()
            return response
        except:
            raise CouldNotConnect("Couldn't connect to the API")
    
# Returns a timetable for a specific stop and line.
    def get_line_timetable(self, stop_id, line):
        try:
            response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={int(stop_id/100)}&busstopNr={str(stop_id)[-2:]}&line={line}&apikey={self.api_key}').json()
            return response
        except:
            raise CouldNotConnect("Couldn't connect to the API")    

# Returns the lines for a number of stops.
    def get_lines_for_stops(self, stop_ids):
        stops_lines = {}
        for stop in stop_ids:
            stop_buses = self.api_adapter.parse_api_lines(self.get_lines_for_stop(stop))
            stops_lines[stop] = stop_buses
        return stops_lines
    
# Returns the timetables for a list of stops.
    def get_timetables_for_stops(self, stop_ids):
        stops_timetables = {}
        stop_lines = self.get_lines_for_stops(stop_ids)
        for stop_id in stop_lines:
            stops_timetables[stop_id] = {}
            for line in stop_lines[stop_id]:
                stops_timetables[stop_id][line] = self.api_adapter.parse_api_timetables(self.get_line_timetable(stop_id, line))
        return stops_timetables

#===================================================API ADAPTER==================================================
# to understand the specific changes done to the data,
# see "Opis api.md" for api response structure
class ApiAdapter:
    def __init__(self):
        pass

    def v(self, thing):
        return thing['value']

# takes in the api response, returns a list of tuples with the stop data
    def parse_api_stops(self, api_stops_response):
        if isinstance(api_stops_response['result'], str):
            raise IncorrectApiCall('Api call failed')
            return None
        stops = []
        for stop_response in api_stops_response['result']:
            stop_response = stop_response['values']
            stop_id = self.v(stop_response[0]) + self.v(stop_response[1])
            stop_name = self.v(stop_response[2])
            stop_geo_1 = self.v(stop_response[4])
            stop_geo_2 = self.v(stop_response[5])
            stop_destination = self.v(stop_response[6])
            stop_data = (stop_id, stop_name, stop_geo_1, stop_geo_2, stop_destination)
            stops.append(stop_data)
        return stops

# takes in the api response, returns a list of lines
    def parse_api_lines(self, api_lines_response):
        if isinstance(api_lines_response['result'], str):
            raise IncorrectApiCall('Api call failed')
            return None
        lines = []
        for line_dict in api_lines_response['result']:
            line_info = line_dict['values']
            for line in line_info:
                lines.append(self.v(line))
        return lines

# takes in the api response, returns a dict with the data
    def parse_api_timetables(self, api_timetables_response):
        if isinstance(api_timetables_response['result'], str):
            raise IncorrectApiCall('Api call failed')
            return None
        time_tables = []
        for time_table in api_timetables_response['result']:
            t_t_i = time_table['values']
            time_table_entr = (self.v(t_t_i[2]), self.v(t_t_i[3]), self.v(t_t_i[4]), self.fix_time(self.v(t_t_i[5])))
            time_tables.append(time_table_entr)
        return time_tables

# For some reason the API thinks it's ok to pass back a time value of "27:22:00"
# I have absolutely zero idea why, but that's how it works so i need a function to fix it.
    def fix_time(self, time):
        # turning arbitrary number of hours into max 24 h
        tms = time.split(':')
        time_delta = timedelta(hours=int(tms[0]), minutes=int(tms[1]), seconds=int(tms[2]))
        # adding the leading zero and returning
        bad = datetime.strptime(str(timedelta(seconds=time_delta.seconds)), '%H:%M:%S')
        return datetime.strftime(bad, '%H:%M:%S')
