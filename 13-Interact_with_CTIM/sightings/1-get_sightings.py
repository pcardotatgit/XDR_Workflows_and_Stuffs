'''
 Get all sightings in your SecureX tenant
'''
import requests
import json
from crayons import *
import config as conf

host = host.conf
item_list=[]

def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    return response
    
def get_sightings(host,access_token):
    fb = open("z_json_sighting_list.json", "w")
    fd = open("z_sightings_id_list.txt", "w")    
    url = "/ctia/sighting/search"
    json_output='[\n'
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        response = get(host,access_token,url,offset,limit)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        print(response.json())    
        items=response.json()
        for item in items: 
            index+=1
            print(yellow(item,bold=True))
            item_list.append(item)
            json_output+=json.dumps(item)
            json_output+=',\n'   
            fd.write(item['id'])
            fd.write('\n')               
        if index>=limit-1:
            go=1
            offset+=index-1
        else:
            go=0
    json_output=json_output[:-2]
    json_output+=']'
    fb.write(json_output)
    fb.close()
    fd.close()
def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    get_sightings(host,access_token)

if __name__ == "__main__":
    main()