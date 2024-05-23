from api_classes import ApiAdapter, ApiFacade, DataObserver
from database_classes import DatabaseAdapter, DatabaseFacade
from datetime import datetime

# Nothing to test here, this is purely for better structure, it doesn't
# do anything on it's own, just calls appropriate methods of the other classes.
def get_key():
    f = open(".env", "r")
    return f.read()

# This is the class that manages how the rest of the program interacts.
class Orchestrator:
    def __init__(self, logger) -> None:
        self.api_face = ApiFacade(get_key(), ApiAdapter())
        self.data_face = DatabaseFacade('tablica.db', DatabaseAdapter())
        self.data_observ = DataObserver()
        self.data_observ.add_subscriber(self.data_face)
        self.logger = logger

# Get the active stop ids from the DB Facade, pass it to the API Facade
# Get the timetables from the API, pass it to the Data Observer
# If the data has changed, the Observer will update the database with the new data.
    def data_collection_cycle(self):
        try:
            stops = self.data_face.get_active_stops_ids()
            dat = self.api_face.get_timetables_for_stops(stops)
            self.data_observ.update(dat)
        except Exception as e:
            self.logger.log(f'{datetime.now()}: Encounterer an Exception with message- {str(e)}')
