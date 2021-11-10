import requests
import json
from collections import defaultdict
from requests.api import request


API_KEY = "721f790d5amsh9617c03735fbb05p19f25bjsne3545c09a53a"
API_URL = "https://unogsng.p.rapidapi.com/"
API_HOST = "unogsng.p.rapidapi.com"

headers = {
    'x-rapidapi-host' : API_HOST,
    'x-rapidapi-key' : API_KEY
}

def get_title (title):
    querystring = {
        "query" : title,
        "orderby": "rating"
    }
    response = requests.request("GET", API_URL + "search", headers=headers, params=querystring)

    
    jsoned = json.loads(response.text)
    jsoned = jsoned["results"]

    results = defaultdict(dict)

    for i in range(len(jsoned)):
        results[i]['nfid'] = jsoned[i]['nfid']
        results[i]['title'] = jsoned[i]['id']
        results[i]['img'] = jsoned[i]['img']
        results[i]['synopsis'] = jsoned[i]['synopsis']
    
    return results



def get_title_location(netflix_id):
    querystring = {
        "netflixid" : netflix_id
    }

    response = requests.request("GET", API_URL + "titlecountries", headers=headers, params=querystring)
    
    jsoned = json.loads(response.text)
    jsoned = jsoned["results"]

    results = defaultdict(dict)


    for i in range(len(jsoned)):
        results[i]['country'] = jsoned[i]['country']
    
    return results
    



#print(get_title_location("80025172"))