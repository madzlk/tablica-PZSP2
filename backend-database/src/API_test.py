import requests
import json
#fa0f3d27-bfbe-40b4-8e77-1b279b68f627 API key
#lewo góra: 52.221459, 21.009006
#lewo dół: 52.216708, 21.009006
#prawo góra: 52.220393, 21.016504
#prawo dół: 52.216673, 21.016076
# 52.221459 >= x >= 52.216673
# 21.016504 >= y >= 21.009006

#t1 = requests.post('https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e927d-4ad3-9500-4ab9e55deb59&type=1&line=523&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627')
#print(t1.json())

response = requests.get("https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId=1001&busstopNr=01&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627").json()
print(response)
with open('88.json', 'w') as f:
    json.dump(response, f)
#print(response.keys())
#print(len(response))
r1 = response['result'] #results of the API call
 # theres 8226
#print(r1)
print(len(r1))
#r2 = r1[0] #a single result
#print(r2)
quit()
#print(len(r2))
#print(r2.keys()) 
#r3 = r2['values'] # entering into the values of a single result
#print(len(r3))
#print(r3)

politechnika_przystanki_temp = []
for f in r1:
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
    if((52.221459 >= float(f['values'][4]['value']) >= 52.216673) and (21.016504 >= float(f['values'][5]['value']) >= 21.009006)):
        politechnika_przystanki_temp.append(f['values'])
        print(f['values'][4]['value']+", "+f['values'][5]['value'])

print(len(politechnika_przystanki_temp))
    
politechnika_przystanki = []
for przystan in politechnika_przystanki_temp:
    id = przystan[0]['value']
    nr = przystan[1]['value']
    nazwa = przystan[2]['value']
    response = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId={id}&busstopNr={nr}&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627')
    print(f'nazwa: {nazwa}, id: {id}, słupek: {nr}')
    print(response.json())
    linie = []
    for r in response.json()['result']:
        linie.append(r['values'][0]['value'])
    politechnika_przystanki.append([nazwa, id, nr, linie])

print(politechnika_przystanki)

for p in politechnika_przystanki:
    nazwa = p[0]
    id = p[1]
    nr = p[2]
    linie = p[3]
    for l in linie:
        response2 = requests.get(f'https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={id}&busstopNr={nr}&line={l}&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627')
        print(response2.json())

#https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e60518c9f3238&busStopId={id}&busStopNr={nr}&line={l}&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627
#https://api.um.warszawa.pl/api/action/dbtimetable_get/?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId=2346&busstopNr=01&line=198&apikey=fa0f3d27-bfbe-40b4-8e77-1b279b68f627
