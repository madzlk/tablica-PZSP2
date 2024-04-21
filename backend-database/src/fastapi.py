from database_classes import DatabaseFacade, DatabaseAdapter
from fastapi import FastAPI

data_face = DatabaseFacade('tablica.db', DatabaseAdapter())
fast_api = FastAPI()

@fast_api.get("/stops")
async def read_stops():
    return data_face.get_active_stops()

@fast_api.get("/times/{stop_id}/{n}")
async def read_times(stop_id, n):
    return data_face.get_n_next_times(stop_id, n)