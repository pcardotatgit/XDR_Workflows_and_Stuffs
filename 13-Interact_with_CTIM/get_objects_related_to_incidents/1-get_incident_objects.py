'''
    Get all incidents in your XDR tenant
    Then you can select one Incident from the list
    
'''
import requests
import json
from crayons import *
import os
import sys

item_list=[]

source_to_select="ALL"

    
def parse_config(text_content):
    text_lines=text_content.split('\n')
    conf_result=['','','','']
    for line in text_lines:
        print(green(line,bold=True))
        if 'ctr_client_id' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[0]=line.split('=')[1]
                conf_result[0]=conf_result[0].replace('"','')
                conf_result[0]=conf_result[0].replace("'","")
                conf_result[0]=conf_result[0].strip()
            else:
                conf_result[0]=""
        elif 'ctr_client_password' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[1]=line.split('=')[1]
                conf_result[1]=conf_result[1].replace('"','')
                conf_result[1]=conf_result[1].replace("'","")
                conf_result[1]=conf_result[1].strip()
            else:
                conf_result[1]=""  
        elif '.eu.amp.cisco.com' in line:
            conf_result[2]="https://visibility.eu.amp.cisco.com"
            conf_result[3]="https://private.intel.eu.amp.cisco.com"
        elif '.intel.amp.cisco.com' in line:
            conf_result[2]="https://visibility.amp.cisco.com"
            conf_result[3]="https://private.intel.amp.cisco.com"            
        elif '.apjc.amp.cisco.com' in line:
            conf_result[2]="https://visibility.apjc.amp.cisco.com"  
            conf_result[3]="https://private.intel.apjc.amp.cisco.com"
    print(yellow(conf_result))
    return conf_result

def get_ctr_token(host_for_token,ctr_client_id,ctr_client_password):
    print(yellow('Asking for new CTR token',bold=True))
    url = f'{host_for_token}/iroh/oauth2/token'
    #url = 'https://visibility.eu.amp.cisco.com/iroh/oauth2/token'
    print()
    print(url)
    print()    
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
    payload = {'grant_type':'client_credentials'}
    print()
    print('ctr_client_id : ',green(ctr_client_id,bold=True))
    print('ctr_client_password : ',green(ctr_client_password,bold=True))
    response = requests.post(url, headers=headers, auth=(ctr_client_id, ctr_client_password), data=payload)
    #print(response.json())
    reponse_list=response.text.split('","')
    token=reponse_list[0].split('":"')
    print(token[1])
    fa = open("ctr_token.txt", "w")
    fa.write(token[1])
    fa.close()
    return (token[1])    
    
def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    if source_to_select=='ALL':
        url = f"{host}{url}?limit={limit}&offset={offset}"
    else:
        url = f"{host}{url}?source={source_to_select}&limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    return response

def clean_result_dir(dirPath):
    #dirPath = './result'
    files =[file for file in os.listdir(dirPath)]
    for file in files:
        print("file to delete : ",file)
        os.remove(dirPath+"/"+file)
    
def get_incidents(host,access_token,client_id,client_password,host_for_token):
    fb = open("./result/z_json_incidents_list.json", "w")
    fd = open("./result/z_incidents_id_list.txt", "w")
    json_output='[\n'
    fc = open("./result/z_incidents_list.txt", "w")
    url = "/ctia/incident/search"
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        response = get(host,access_token,url,offset,limit)
        print(response)      
        if response.status_code==401:
            access_token=get_ctr_token(host_for_token,client_id,client_password)
            response = get(host,access_token,url,offset,limit)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        #print(response.json())    
        print()
        print(yellow('Incidents into the XDR Tenant :',bold=True))
        items=response.json()
        for item in items: 
            #print(yellow(item,bold=True))
            if item['id'] not in item_list:
                item_list.append(item['id'])
            #fb.write(json.dumps(item))
            #fb.write(',\n')
            json_output+=json.dumps(item)
            json_output+=',\n'
            fc.write(item['title']+' ; '+item['id'])
            fc.write('\n')   
            fd.write(item['id'])
            fd.write('\n')   
            print(str(index),' : ',item['title'])    
            index+=1            
        if index>=limit-1:
            go=1
            offset+=index-1
        else:
            go=0
    json_output=json_output[:-2]
    json_output+=']'
    fb.write(json_output)
    fb.close()
    fc.close()
    fd.close()    
    i=0
    print()
    a=input('Which Incident do you select ? ( enter incident index ) : ')
    index=int(a)
    #print()
    #print(item_list[index])
    return (item_list[index])

def get_sightings(host,access_token,sighting_id):
    print(sighting_id)
    fd = open("./result/z_sightings_id_list.txt", "a+")
    file_name=sighting_id.split(':443/')[1]
    file_name='./result/'+file_name.replace('/','-')+'.json' 
    #print(file_name)
    fb = open(file_name, "w")  
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}    
    json_output=''
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        url = f"{host}/ctia/sighting/search?id={sighting_id}&limit={limit}&offset={offset}"
        response = requests.get(url, headers=headers)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        print(payload)    
        items=response.json()
        for item in items: 
            index+=1
            print(yellow(item,bold=True))
            item_list.append(item)
            json_output+=json.dumps(item)
            json_output+=',\n'    
            fd.write(item['id']+'\n')
        if index>=limit-1:
            go=1
            offset+=index-1
        else:
            go=0
    json_output=json_output[:-2]
    #json_output+=']'
    fb.write(json_output)
    fb.close()
    fd.close()
    
def get_relationships(host,access_token,target_ref):
    sighting_list=[]
    fb = open("./result/z_json_relationships_list.json", "w")
    fd = open("./result/z_relationships_id_list.txt", "w")
    json_output='[\n'
    fc = open("./result/z_relationships_list.txt", "w")    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        url = f"{host}/ctia/relationship/search?target_ref={target_ref}&limit={limit}&offset={offset}"
        response = requests.get(url, headers=headers)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        #print(payload)    
        items=response.json()
        for item in items: 
            index+=1
            #print(yellow(item,bold=True))
            print("Sighting ID :",yellow(item['source_ref'],bold=True))
            item_list.append(item)
            #fb.write(json.dumps(item))
            #fb.write(',\n')
            json_output+=json.dumps(item)
            json_output+=',\n'
            fc.write('\n')   
            fd.write(item['id'])
            fd.write('\n')  
            get_sightings(host,access_token,item['source_ref'])
        if index>=limit-1:
            go=1
            offset+=index-1
        else:
            go=0
    json_output=json_output[:-2]
    json_output+=']'
    fb.write(json_output)
    fb.close()
    fc.close()
    fd.close()
    return (sighting_list)
    
def main():
    with open('config.txt','r') as file:
        text_content=file.read()
    host = parse_config(text_content)
    client_id,client_password,host_for_token,host = parse_config(text_content)
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()
    print()
    print(yellow('STEP 0 - Clean previous results',bold=True))
    print()
    clean_result_dir('./result')
    print()
    print(yellow('STEP 1 - Select Incident',bold=True))
    print()
    incident_ID=get_incidents(host,access_token,client_id,client_password,host_for_token)
    print()
    print("Selected Incident is : \n",cyan(incident_ID,bold=True))
    with open("./result/z_incidents_id_list.txt", "w") as fd:
        fd.write(incident_ID)
    print()
    print(yellow('STEP 2 - Get Every Incident Relationships and sightings',bold=True))
    print()
    sighting_list=get_relationships(host,access_token,incident_ID) 
    print()

if __name__ == "__main__":
    main()
