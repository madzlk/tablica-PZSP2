import requests
import json
from api_classes import ApiAdapter, ApiFacade
from database_classes import DatabaseFacade, DatabaseObserver, DatabaseAdapter

#fa0f3d27-bfbe-40b4-8e77-1b279b68f627 API key
#lewo góra: 52.221459, 21.009006
#lewo dół: 52.216708, 21.009006
#prawo góra: 52.220393, 21.016504
#prawo dół: 52.216673, 21.016076
# 52.221459 >= x >= 52.216673
# 21.016504 >= y >= 21.009006

api_adp = ApiAdapter()
dat_adp = DatabaseAdapter()
api_face = ApiFacade('fa0f3d27-bfbe-40b4-8e77-1b279b68f627', api_adp)
dat_face = DatabaseFacade('tablica.db')
dat_obs = DatabaseObserver(dat_face)

stops = dat_adp.parse_database_stop_ids(dat_face.get_active_stops_id())
print('got stop ids')
timetables = api_face.get_timetables_for_stops(stops)
print('got timetable from api')
dat_face.set_timetables(timetables)
print(dat_obs.prepare_database_hash())
stops = dat_adp.parse_database_stop_ids(dat_face.get_active_stops_id())
print('got stop ids')
timetables = api_face.get_timetables_for_stops(stops)
print('got timetable from api')
dat_face.set_timetables(timetables)
print(dat_obs.prepare_database_hash())

politechnika_przystanki_temp = []
#for f in r1:
   # if(f['values'][2]['value'] == 'Torfowa'):
        #print(f['values'])
        #id = f['values'][0]['value']
        #nr = f['values'][1]['value']
        #response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId={id}&busstopNr={nr}&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627')
        #print(response.json())
        #for i in response.json()['result']:
         #   l = i['values'][0]['value']
         #   r2 = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e60518c9f3238&busstopId={id}&busstopNr={nr}&line={l}&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627')
        #    print(r2.json())
    #if((52.222 >= float(f['values'][4]['value']) >= 52.215) and (21.017 >= float(f['values'][5]['value']) >= 21.000)):
     #   politechnika_przystanki_temp.append(f['values'])
        #print(f['values'][4]['value']+", "+f['values'][5]['value'])

