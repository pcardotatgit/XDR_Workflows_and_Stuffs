'''
    Get incident-summary 
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
    print(yellow(url))
    response = requests.get(url, headers=headers)
    return response

def clean_result_dir(dirPath):
    #dirPath = './result'
    files =[file for file in os.listdir(dirPath)]
    for file in files:
        print("file to delete : ",file)
        os.remove(dirPath+"/"+file)
           
def get_incident_summary(host,access_token):
    indicator_id_list=[]
    fb = open("./result/incident-summary.json", "w")
    #fd = open("./result/indicators_id_list.txt", "w")
    json_output='[\n'
    #fc = open("./result/indicators_list.txt", "w")    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    offset=0
    limit=1000
    go=1 # used to stop the loop  
    incident_id="https://private.intel.eu.amp.cisco.com:443/ctia/incident/incident-da3d4b10-a653-4274-89b3-136a5c2f835d"
    while go:      
        index=0
        url = f"{host}/iroh/private-intel/incident-summary/search?id={incident_id}"
        response = requests.get(url, headers=headers)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        #print(yellow(payload,bold=True))    
        items=response.json()
        for item in items: 
            index+=1
            #print(yellow(item,bold=True))
            #print()
            #print("Indicator name :",yellow(item['title'],bold=True))
            indicator_id_list.append(item['title'])
        if index>=limit-1:
            go=1
            offset+=index-1
        else:
            go=0
    fb.write(payload)
    fb.close()
    return (indicator_id_list)

    
def read_ctr_token():
    with open('ctr_token.txt','r') as file:
        token=file.read()
    return(token)
    
def get_incidents(host,access_token,client_id,client_password,host_for_token):
    fb = open("./result/z_json_incidents_list.json", "w")
    fd = open("./result/z_incidents_id_list.txt", "w")
    #fb.write('[\n')
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
    
def get_incident_summary(host,access_token,incident_id):
    indicator_id_list=[]
    incident_dir_path='result'
    fb = open('./'+incident_dir_path+'/incident-summary.json', "w")
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}/iroh/private-intel/incident-summary/search?id={incident_id}"
    response = requests.get(url, headers=headers)
    payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
    #print(yellow(payload,bold=True))   
    items=response.json()
    index=0
    if len(items)>0:
        for item0 in items[0]['context']['indicators']: 
            print("Indicator :",yellow(item0["title"] ,bold=True))
            print(green(item0,bold=True))        
            indicator_id_list.append(item0['title'])
            payload2 = json.dumps(item0,indent=4,sort_keys=True, separators=(',', ': '))
            with open('./'+incident_dir_path+'/indicator_'+str(index)+'.json', "w") as fichier:
                fichier.write(payload2)
            index+=1
        index=0
        # here under indicators relationships of this incident
        for item0 in items[0]['context']['relationships']: 
            print(green(item0,bold=True))
            #print()
            #print("Indicator name :",yellow(item['title'],bold=True))
            if item0["relationship_type"] =='sighting-of':
                payload2 = json.dumps(item0,indent=4,sort_keys=True, separators=(',', ': '))
                with open('./'+incident_dir_path+'/indicator_relationship_'+str(index)+'.json', "w") as fichier:
                    fichier.write(payload2)
            index+=1
        # here under incident sightings and sightings observables relationships of this incident  [0]["context"]["sightings"][0]["relations"][0] 
        for item0 in items[0]['context']['sightings']: 
            print(green(item0,bold=True))
            sighting_id=item0["id"]         
            file_name=sighting_id.split(':443/')[1]
            file_name=file_name.replace('/','-')
            file_name=file_name.replace('ctia-sighting-','')
            subdir=incident_dir_path+'/sightings/'+file_name
            os.mkdir(subdir)
            # here under incident sightings
            file_name=file_name+'.json' 
            payload2 = json.dumps(item0,indent=4,sort_keys=True, separators=(',', ': '))        
            with open('./'+subdir+'/'+file_name, "w") as fichier:
                fichier.write(payload2)
            # here under sighting observables
            if 'observables' in item0.keys():
                payload2 = json.dumps(item0['observables'],indent=4,sort_keys=True, separators=(',', ': '))
                with open('./'+subdir+'/observables.json', "w") as fichier:
                    fichier.write(payload2)
            # here under sighting  observables relationships
            if 'relations' in item0.keys():
                payload2 = json.dumps(item0['relations'],indent=4,sort_keys=True, separators=(',', ': '))
                with open('./'+subdir+'/relationships.json', "w") as fichier:
                    fichier.write(payload2)  
            # here under sighting  targets
            if 'targets' in item0.keys():
                payload2 = json.dumps(item0['targets'],indent=4,sort_keys=True, separators=(',', ': '))
                with open('./'+subdir+'/targets.json', "w") as fichier:
                    fichier.write(payload2) 
    fb.write(payload)
    fb.close()
    return (1)
    
def main():
    print()
    print(yellow('STEP 1 - Read Config.txt',bold=True))
    with open('config.txt','r') as file:
        text_content=file.read()
    print(yellow('STEP 2 - Ask for a CTR TOKEN',bold=True))
    client_id,client_password,host_for_token,host = parse_config(text_content)
    #access_token=get_ctr_token(host_for_token,client_id,client_password)
    access_token=read_ctr_token()
    print(yellow('STEP 3 - Select an Incident',bold=True))
    print()
    incident_ID=get_incidents(host,access_token,client_id,client_password,host_for_token)
    print()
    print("---- Selected Incident is : \n",cyan(incident_ID,bold=True))
    print()
    a=input('type enter to continue')
    print()
    print(yellow('STEP 4 - Get selected Incident Details',bold=True))
    print()    
    get_incident_summary(host_for_token,access_token,incident_ID)
    print()
if __name__ == "__main__":
    main()
