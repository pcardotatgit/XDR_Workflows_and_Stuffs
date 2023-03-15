'''
    Create a bundle incident + sightings + relationship from incident-2.json file
'''
import requests
import json
from crayons import *
import config as conf

host=conf.host

item_list=[]

def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    return response

def create_bundle(host,access_token):
    with(open("incident-2.json","r")) as file:
        incident_txt=file.read()
    incident_json=json.loads(incident_txt)
    print(incident_json)
    print()
    print("Let's connect to CTIA")
    print()
    url = f"{host}/ctia/bundle/import" 
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=incident_json,headers=headers)
    print()
    print("Ok Done")
    print()    
    print(response)
    return 1
    
def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    create_bundle(host,access_token)

if __name__ == "__main__":
    main()
