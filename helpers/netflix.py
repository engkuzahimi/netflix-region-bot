import requests
import json
from collections import defaultdict
from requests.api import request
import re
import location


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
        "orderby": "rating",
        "limit": 10
    }
    response = requests.request("GET", API_URL + "search", headers=headers, params=querystring)

    
    jsoned = json.loads(response.text)
    jsoned = jsoned["results"]

    results = defaultdict(dict)

    for i in range(len(jsoned)):
        g = None
        g = re.search(title, jsoned[i]['title'], re.IGNORECASE)
        if (g != None):
            results[0]['nfid'] = jsoned[i]['nfid']
            results[0]['title'] = jsoned[i]['title']
            results[0]['img'] = jsoned[i]['img']
            results[0]['synopsis'] = jsoned[i]['synopsis']
            break
    
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
    


tajuk = get_title("parks and recreation")
print(tajuk)

tajuk = get_title_location(tajuk[0]['nfid'])