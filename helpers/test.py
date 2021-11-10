from location import calculate_distance
import json

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

A = {0: {'country': 'United Kingdom', 'coordinates': '54.7023545,-3.2765753'}, 1: {'country': 'France ', 'coordinates': '46.603354,1.8883335'}, 2: {'country': 'Australia ', 'coordinates': '-24.7761086,134.755'}, 3: {'country': 'Belgium ', 'coordinates': '50.6402809,4.6667145'}}
B = []

#1. Get coordinates only
for i in A:
    B.append(A[i]['coordinates'])

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

for i in range(len(B)):
    #clear counter if exceed 10
    F = 1
    if i > CHUNKS_NUM - 1:
        D.clear()
        j = 1

    for j in range(CHUNKS_NUM):
        try:
            D['end_point_' + str(j + 1)] = B[i][j]
        except IndexError:
            break
    E = E | D
    
    
    response = calculate_distance(E)

    jsoned = json.loads(response.text)

    for k in range(2, len(jsoned)):
        H = jsoned["end_point_{}".format(F)]['distance']
        A[F - 1]['distance'] = H
        F = F + 1
        


    

#print(A)