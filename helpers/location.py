from geopy import Nominatim
import requests
from netflix import API_KEY
from collections import OrderedDict
import json

locations_test = {0: {'country': 'Malaysia'}, 1: {'country': 'France '}, 2: {'country': 'Australia '}, 3: {'country': 'Belgium '}, 4: {'country': 'Canada '}}

def location_to_coordinates (locations):
    locator = Nominatim(user_agent="myGeocoder")
    

    for i in range(len(locations)):
        location = locator.geocode(locations[i]['country'])
        locations[i]['coordinates'] = "{},{}".format(location.latitude,location.longitude)
    
    return locations
   

def fetch_distance (querystring):
    API_URL = "https://distance-calculator.p.rapidapi.com/v1/one_to_many"
    API_HOST = "distance-calculator.p.rapidapi.com"

    headers = {
        'content-type' : "application/json",
        'x-rapidapi-host' : API_HOST,
        'x-rapidapi-key' : API_KEY
    }
    

    response = requests.request("GET", API_URL, headers=headers, params=querystring)
    return response


def calculate_distance (locations):
    
    A = locations
    B = []

    #1. Get coordinates only
    for i in locations:
        B.append(locations[i]['coordinates'])

    #10 chunks
    CHUNKS_NUM = 2

    #SPLIT
    B = list(chunks(B,CHUNKS_NUM))


    D = {} #temporary

    MY_COORD = "4.5693754,102.2656823"

    E = {
            "start_point" : MY_COORD,
            "unit" : "kilometers",
            "decimal_places" : "2",
        }#payload

    F = 0
    for i in range(len(B)):

        #clear counter if exceed 10
    
        if i > CHUNKS_NUM - 1:
            D.clear()
            j = 1

        for j in range(CHUNKS_NUM):
            try:
                D['end_point_' + str(j + 1)] = B[i][j]
            except IndexError:
                break
        E = E | D
        
        
        response = fetch_distance(E)

        jsoned = json.loads(response.text)


        for k in range(1,3):
            
            H = jsoned["end_point_{}".format(k)]['distance']
            try:
                locations[F]['distance'] = H   
            except(KeyError):
                break
            F = F + 1

    sortedd = sorted(locations, key=lambda x: (locations[x]['distance'])) 
    return sortedd

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

hello = location_to_coordinates(locations_test)

hello = calculate_distance(hello)

print(hello)
