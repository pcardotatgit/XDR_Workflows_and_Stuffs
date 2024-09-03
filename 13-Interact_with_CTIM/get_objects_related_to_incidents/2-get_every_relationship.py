'''
    Get all incidents from your XDR tenant
    Next Select one of them
    Then every Incident objects are saved into the ./result  subfolder
    
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
    
def read_ctr_token():
    with open('ctr_token.txt','r') as file:
        token=file.read()
    return(token)
    
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
        
def get_relationships(host,access_token):
    sighting_list=[]
    fb = open("./result/relationships_list.json", "w")
    fd = open("./result/relationships_id_list.txt", "w")
    json_output='[\n'
    fc = open("./result/z_relationships_list.txt", "w")    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        url = f"{host}/ctia/relationship/search?limit={limit}&offset={offset}"
        response = requests.get(url, headers=headers)
        #payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        #print(payload)    
        items=response.json()
        for item in items: 
            index+=1
            print(yellow(item,bold=True))
            #print("Sighting ID :",yellow(item['source_ref'],bold=True))
            item_list.append(item)
            fb.write(json.dumps(item))
            fb.write(',\n')
            json_output+=json.dumps(item)
            json_output+=',\n'
            fc.write('\n')   
            #fd.write(item['id'])
            #fd.write('\n')  
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
    print()
    print(yellow('STEP 1 - Read Config.txt',bold=True))
    with open('config.txt','r') as file:
        text_content=file.read()
    print(yellow('STEP 2 - Ask for a CTR TOKEN',bold=True))    
    client_id,client_password,host_for_token,host = parse_config(text_content)
    #access_token=get_ctr_token(host_for_token,client_id,client_password)
    access_token=read_ctr_token()
    print()
    print(yellow('STEP  - Get Every Relationships',bold=True))
    print()
    get_relationships(host,access_token) 
    print()

if __name__ == "__main__":
    main()
