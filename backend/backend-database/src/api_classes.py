import requests
import datetime

class ApiFacade:
    def __init__(self, api_key, api_adapter):
        self.api_key = api_key
        self.api_adapter = api_adapter

    def get_all_stops(self):
        response = self.api_adapter.parse_api_stops(requests.get(f'https://api.um.warszawa.pl/api/action/dbstore_get?id=ab75c33d-3a26-4342-b36a-6e5fef0a3ac3&apikey={self.api_key}').json())
        return response

    def get_lines_for_stop(self, stop_id):
        response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId={int(stop_id/100)}&busstopNr={str(stop_id)[-2:]}&apikey={self.api_key}').json()
        return response
    
    def get_line_timetable(self, stop_id, line):
        response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={int(stop_id/100)}&busstopNr={str(stop_id)[-2:]}&line={line}&apikey={self.api_key}').json()
        return response
    
    def get_lines_for_stops(self, stop_ids):
        stops_lines = {}
        for stop in stop_ids:
            stop_buses = self.api_adapter.parse_api_lines(self.get_lines_for_stop(stop))
            stops_lines[stop] = stop_buses
        return stops_lines
    
    def get_timetables_for_stops(self, stop_ids):
        stops_timetables = {}
        stop_lines = self.get_lines_for_stops(stop_ids)
        for stop_id in stop_lines:
            stops_timetables[stop_id] = {}
            for line in stop_lines[stop_id]:
                stops_timetables[stop_id][line] = self.api_adapter.parse_api_timetables(self.get_line_timetable(stop_id, line))
        return stops_timetables

# to understand the specific changes done to the data,
# see "Opis api.md" for api response structure
class ApiAdapter:
    def __init__(self):
        pass

    def v(self, thing):
        return thing['value']

# takes in the api response, returns a list of tuples with the stop data
    def parse_api_stops(self, api_stops_response):
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
        lines = []
        for line_dict in api_lines_response['result']:
            line_info = line_dict['values']
            for line in line_info:
                lines.append(self.v(line))
        return lines

# takes in the api response, returns a dict with the data
    def parse_api_timetables(self, api_timetables_response):
        time_tables = []
        for time_table in api_timetables_response['result']:
            t_t_i = time_table['values']
            time_table_entr = (self.v(t_t_i[2]), self.v(t_t_i[3]), self.v(t_t_i[4]), self.fix_time(self.v(t_t_i[5])))
            time_tables.append(time_table_entr)
        return time_tables

    def fix_time(self, time):
        tms = time.split(':')
        time_delta = datetime.timedelta(hours=int(tms[0]), minutes=int(tms[1]), seconds=int(tms[2]))
        return str(datetime.timedelta(seconds=time_delta.seconds))