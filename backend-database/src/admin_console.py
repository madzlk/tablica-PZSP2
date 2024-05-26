from api_classes import ApiAdapter, ApiFacade, DataObserver
from database_classes import DatabaseAdapter, DatabaseFacade
import os
from datetime import datetime

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_key():
    f = open(".env", "r")
    return f.read()

class Square():
    def __init__(self, max_lat, min_lat, max_lon, min_lon):
        self.max_lat = max_lat
        self.min_lat = min_lat
        self.max_lon = max_lon
        self.min_lon = min_lon
    
    def check_if_in(self, lat, lon):
        if self.max_lat>=lat>=self.min_lat and self.max_lon>=lon>=self.min_lon:
            return True
        return False

class AdminConsole():
    def __init__(self, db_face, api_face):
        self.db_face = db_face
        self.api_face = api_face
        self.stops = self.api_face.get_all_stops()

    def main(self):
        while(True):
            cls()
            act = input("Please select which action you would like to perform: (type number)\n"+
                           "1.Change Stops Configuration\n"+
                           "2.Remove Stop\n"+
                           "3.Add Stop\n"+
                           "4.Quit\n")
            if act == '1':
                while(True):
                    cls()
                    self.print_stops(self.db_face.get_stops())
                    stop = input("Type stop id to change a stops' status, or 'e' to return to main menu\n")
                    if stop == 'e':
                        break
                    if not stop.isnumeric():
                        input('Stop id not recognized. press enter to continue.\n')
                        continue
                    else:
                        stat = input("Choose new status (0 or 1)\n")
                        if not(stat == '0' or stat =='1'):
                            input('Incorrect status entered. press enter to continue.\n')
                            continue
                        else:
                            self.toggle_stop(int(stop), stat)
                continue
            if act == '2':
                while(True):
                    cls()
                    self.print_stops(self.db_face.get_stops())
                    stop = input("Type stop id to remove a stop from the database, or 'e' to return to main menu\n"+
                                 "(Removing a stop is permanent! Consider setting the status to '0' instead.)\n")
                    if stop == 'e':
                        break
                    if not stop.isnumeric():
                        input('Stop id not recognized. press enter to continue.\n')
                        continue
                    else:
                        self.db_face.remove_stop(int(stop))
                continue
            if act == '3':
                while(True):
                    cls()
                    opt = input("Choose how you'd like to find a stop in the city's database, or 'e' to return to main menu:\n"+
                                "1.Find by name\n"+
                                "2.Find by geographic coordinates\n")
                    if opt == 'e':
                        break
                    if opt == '1':
                        name = input("Please type in the name you'd like to find\n")
                        stops = self.find_stops_by_name(name)
                        self.choose_stop_to_add(stops)
                    if opt == '2':
                        square = self.get_square()
                        if square is None:
                            input('Incorrect coordinates. press enter to continue.')
                            continue
                        stops = self.find_stops_by_square(square)
                        self.choose_stop_to_add(stops)
                continue
            if act == '4':
                break
            else:
                input('option not recognized,\n Please write only the number of the option you would like to choose.\n press enter to continue.\n')

    def print_stops(self, stops):
        for s in stops:
            print(f'{s[1]}. {s[2]} {s[0]}, aktywny:{s[8]}')

    def print_new_stops(self, stops):
        for id, s in enumerate(stops):
            print(f'{id}: {s}')

    def toggle_stop(self, stopid, status):
        self.db_face.set_active_inactive(stopid, status)

    def get_square(self):
        while(True):
            lat1= input('Input first latitude (North or South)\n')
            lat2= input('Input second latitude (North or South)\n')
            lon1= input('Input first longitude (West or East)\n')
            lon2= input('Input second longitude (West or East)\n')
            try:
                lat1 = float(lat1)
                lat2 = float(lat2)
                lon1 = float(lon1)
                lon2 = float(lon2)
                sqr = Square(max([lat1, lat2]), min([lat1, lat2]), max([lon1, lon2]), min([lon1, lon2]))
                return sqr
            except:
                return None

    def find_stops_by_name(self, name):
        g_stops = []
        for s in self.stops:
            if name in s[1]:
                g_stops.append(s)
        return g_stops

    def find_stops_by_square(self, square):
        g_stops = []
        for s in self.stops:
            #print(f'checking if {s[2]}, {s[3]} in square')
            if square.check_if_in(s[2], s[3]):
                g_stops.append(s)
        return g_stops

    def add_stop_to_db(self, stop_to_add):
        new_id = self.db_face.get_stops()[-1][1]+1
        dist = input('Please enter the walking distance of the stop\n')
        new_stop_data = (int(stop_to_add[0]), int(new_id), stop_to_add[1], float(stop_to_add[2]), float(stop_to_add[3]), int(dist), stop_to_add[4], str(datetime.now()), '1')
        confirm = input(f'Please confirm if the stop data is correct (Y/N):\n{new_stop_data}\n')
        if confirm == "Y":
            self.db_face.add_stop(new_stop_data)
        if confirm == "N":
            return
        else:
            input('incorrect option, press enter to continue.')
            return
        
    def choose_stop_to_add(self, stops):
        print('Found stops:')
        self.print_new_stops(stops)
        id = input('Please choose which stop you would like to add.\n')
        if not id.isnumeric():
            input('Incorrect id entered. press enter to continue.')
            return
        stop_to_add = stops[int(id)]
        self.add_stop_to_db(stop_to_add)

adm = AdminConsole(DatabaseFacade('tablica.db', DatabaseAdapter()), ApiFacade(get_key(), ApiAdapter()))
adm.main()