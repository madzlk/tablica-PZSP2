from database_classes import DatabaseFacade, DatabaseAdapter
from fastapi import FastAPI

data_face = DatabaseFacade('tablica.db', DatabaseAdapter())
fast_api = FastAPI()

# Nothing to test here since this is all completely unpure, test have to be more complex than
# unit tests.

# It's worth noting that this works because all connections and cursors
# are closed after being used by the database facade, and as such,
# while sqlite doesn't allow concurrency easily, we have what could be percieved as concurrency
# simply because when the other cursor is done, our new one gets it's turn.

# simply uses the method of the Database Facade
@fast_api.get("/stops")
async def read_stops():
    return data_face.get_active_stops()

# simply uses the method of the Database Facade
@fast_api.get("/times/{stop_id}/{n}")
async def read_times(stop_id, n):
    return data_face.get_n_next_times(int(stop_id), int(n))