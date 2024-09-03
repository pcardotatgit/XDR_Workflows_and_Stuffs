'''
    Get all judgements in your private intelligence from a source = Patrick_Example
        This source is actually the name of the TOR entry / exit IP addresses List stored into SecureX Judgments
    Then collect the current TOR entry / exit IP addresses List from INTERNET
    - Then Remove from SecureX Judgments all IP addresses which don't exist into the current TOR entry / exit IP addresses List
    - And add into SecureX Judgments new IP addresses found into the current TOR entry / exit IP addresses List
    - create relationships with indicators and feeds for every observables.Then observable will appear into SecureX blocking list
    - Manages the Token request and expiration
'''
import requests
import json
from crayons import *
import config as conf
import sys
import time
from datetime import datetime, timedelta

ctr_client_id=conf.ctr_client_id
ctr_client_password=conf.ctr_client_password
host_for_token=conf.host_for_token
host=conf.host

source_to_select="check.torproject.org"

DISPOSITIONS = {
    'clean': (1, 'Clean'),
    'malicious': (2, 'Malicious'),
    'suspicious': (3, 'Suspicious'),
    'common': (4, 'Common'),
    'unknown': (5, 'Unknown')
}

def read_api_keys(service):   
    # read API credentials from an external file on this laptop ( API keys are not shared with the flask application )
    if service=="webex":
        with open('../keys/webex_keys.txt') as creds:
            text=creds.read()
            cles=text.split('\n')
            ACCESS_TOKEN=cles[0].split('=')[1].strip()
            ROOM_ID=cles[1].split('=')[1].strip()
            #print(ACCESS_TOKEN,ROOM_ID) 
            return(ACCESS_TOKEN,ROOM_ID)
    if service=="ctr":
        if ctr_client_id=='paste_CTR_client_ID_here':
            with open('../keys/ctr_api_keys.txt') as creds:
                text=creds.read()
                cles=text.split('\n')
                client_id=cles[0].split('=')[1]
                client_password=cles[1].split('=')[1]
                #access_token = get_token()
                #print(access_token) 
        else:
            client_id=ctr_client_id
            client_password=ctr_client_password
        return(client_id,client_password)
    if service=="kenna":
        if kenna_token=='paste_kenna_token_here':
            with open('../keys/kenna.txt') as creds:
                access_token=creds.read()
                #print(access_token)          
        else:
            access_token=kenna_token   
        return(access_token)
        
def get_token():
    print()
    print(cyan('Asking for a new Token',bold=True))
    print()
    url = f'{host_for_token}/iroh/oauth2/token'
    print('host :',url)
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
    payload = {'grant_type':'client_credentials'}
    client_id,client_password=read_api_keys('ctr') 
    print(client_id)
    print(client_password)   
    print()
    #sys.exit()
    response = requests.post(url, headers=headers, auth=(client_id, client_password), data=payload)
    print('status code :',response.status_code) 
    print()
    #print(yellow(response.json()))
    print(response.text)
    #print()
    #sys.exit()
    if response.status_code==200:
        reponse_list=response.text.split('","')
        token=reponse_list[0].split('":"')
        print(green(token[1],bold=True))
        fa = open("ctr_token.txt", "w")
        fa.write(token[1])
        fa.close()
        return(token[1])
    else:
        print(red("Error check your client-ID, Client-password and host",bold=True))
        sys.exit()

def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    if response.status_code==401:   
        print(red('ask again for a token'))
        access_token=get_token()
        headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
        response = requests.get(url, headers=headers)
    return response
    
def get_with_query_params(host,access_token,url,query,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}&query={query}"
    #print('url',cyan(url,bold=True))
    response = requests.get(url, headers=headers)
    if response.status_code==401:   
        print(red('ask again for a token'))
        access_token=get_token()
        headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
        response = requests.get(url, headers=headers)
    #print(cyan('response :',bold=True))
    #print(cyan(response.json(),bold=True))       
    return response

def get_judgments(access_token):
    #json_output='[\n'
    url = "/ctia/judgement/search"
    tor_dict={}
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        response = get(host,access_token,url,offset,limit)
        if response.status_code!=401:
            payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
            print(response.json())    
            items=response.json()
            for item in items: 
                index+=1
                if item['source']==source_to_select:
                    print(yellow(item,bold=True))
                    ip=item['observable']['value']    
                    print(red(ip,bold=True))
                    tor_dict[ip]=item['id']
            if index>=limit-1:
                go=1
                offset+=index-1
            else:
                go=0
        else:
            # renew the token and send again the request
            access_token=get_token()
            response = get(host,access_token,url,offset,limit)
            if response.status_code!=401:
                payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
                print(response.json())    
                items=response.json()
                for item in items: 
                    index+=1
                    if item['source']==source_to_select:
                        print(yellow(item,bold=True))
                        ip=item['observable']['value']    
                        print(red(ip,bold=True))
                        tor_dict[ip]=item['id']
                if index>=limit-1:
                    go=1
                    offset+=index-1
                else:
                    go=0            
    return(tor_dict)

def get_indicators(access_token):
    #json_output='[\n'
    url = "/ctia/indicator/search"
    #tor_dict={}
    offset=0
    limit=1000
    local_indicator_list=[]
    query_list=['title:Secure_Firewall_SecureX_Indicator_SHA256','title:Secure_Firewall_SecureX_Indicator_IPv4','title:Secure_Firewall_SecureX_Indicator_IPv6','title:Secure_Firewall_SecureX_Indicator_URL','title:Secure_Firewall_SecureX_Indicator_Domain']
    for indic in query_list:
        go=1 # used to stop the loop   
        print(red(indic))
        while go:      
            index=0
            response = get_with_query_params(host,access_token,url,indic,offset,limit)
            #print('response :')
            #print(response.json())
            #sys.exit()
            if response.status_code!=401:
                payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
                #print(response.json()) 
                items=response.json()
                for item in items: 
                    indicator_dict={}
                    indicator_dict[item['title']]=item['id']
                    local_indicator_list.append(indicator_dict)
                if index>=limit-1:
                    go=1
                    offset+=index-1
                else:
                    go=0
            else:
                # renew the token and send again the request
                access_token=get_token()
                response = get(host,access_token,query,url,offset,limit)
                if response.status_code!=401:
                    payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
                    #print(response.json()) 
                    items=response.json()
                    for item in items: 
                        indicator_dict={}
                        indicator_dict[item['title']]=item['id']
                        local_indicator_list.append(indicator_dict)
                    if index>=limit-1:
                        go=1
                        offset+=index-1
                    else:
                        go=0  
    print('indicator list :',red(local_indicator_list,bold=True))
    return(local_indicator_list)    

def create_relationship_for_feed(access_token,judgment_id,indicator_id,observable):
    print(yellow('New step : create JSON payload for relationship',bold=True))
    # Get the current date/time
    dateTime = datetime.now()
    # Build the relationship object
    relationship_object = {}
    relationship_object["description"] = "SecureX feeds relationship"
    relationship_object["schema_version"] = "1.0.11"
    relationship_object["target_ref"] = indicator_id
    relationship_object["type"] = "relationship"
    relationship_object["source"] = "securex-orchestration"
    relationship_object["short_description"] = "SecureX feeds relationship"
    relationship_object["title"] = f"reliationship_for_{observable}"
    relationship_object["source_ref"] = judgment_id
    relationship_object["tlp"] = "green"
    relationship_object["timestamp"] = dateTime.strftime("%Y-%m-%dT%H:%M:%SZ")
    relationship_object["relationship_type"] = 'element-of'
    print()
    print('relationship :',green(relationship_object,bold=True))
    print()
    print(yellow(' OK DONE',bold=True))
    print()
    print(yellow('New step : POST relationship to secureX',bold=True))
    url = f'{host}/ctia/relationship'
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    payload = json.dumps(relationship_object)
    response = requests.post(url, headers=headers, data=payload)   
    print()
    print (yellow(response,bold=True))  
    print()    
    return 1
   
    
def current_date_time():
    '''
        current time in the format : YYYY-mm-ddTH:M:S.fZ
    '''
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return(current_time)
    
def date_plus_x_days(nb): 
    '''
        current date and time + nb days . In the format : YYYY-mm-ddTH:M:S.fZ
    ''' 
    current_time = datetime.utcnow()
    start_time = current_time + timedelta(days=nb)
    timestampStr = start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return(timestampStr)
    
def add_secureX_judgment_for_this_ip(access_token,ip):
    '''
        generate dynamically the JSON payload for SecureX Judgment and POST it to Threat Response
    '''
    # Create header
    start_time=current_date_time()
    end_time=date_plus_x_days(7)
    judgment_json={"type": "judgement","schema_version": "1.1.3"}
    judgment_json["valid_time"]={
        "start_time": start_time,
        "end_time": end_time
    }
    judgment_json["observable"] = {
    "value": ip,
    "type": "ip"
    }
    judgment_json["source"] = "Patrick_Example"
    disposition='malicious'
    judgment_json["disposition"] = DISPOSITIONS[disposition][0]
    judgment_json["reason"] = "IP from TOR entry / exit IP list"    
    judgment_json["source_uri"] = "https://check.torproject.org/torbulkexitlist" 
    judgment_json["disposition_name"] = DISPOSITIONS[disposition][1]   
    judgment_json["severity"] ="Medium"
    judgment_json["tlp"] ="green"
    judgment_json["timestamp"] =start_time
    judgment_json["confidence"] ="High" 
    judgment_json["priority"] =90   
    '''
    print()
    print(cyan(judgment_json,bold=True))
    print()
    sys.exit()
    '''
    url = f'{host}/ctia/judgement'
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    payload = json.dumps(judgment_json)
    response = requests.post(url, headers=headers, data=payload)
    judgment_id=response.json()['id']
    '''
    print()
    print (yellow(response,bold=True))  
    print()
    print('id :',green(indicator_id,bold=True))
    print()
    '''
    return(judgment_id)

def get_last_tor_blocking_list(tor_dict):
    '''
        Get TOR IP List and update SecureX Judgments      
    '''  
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}    
    print()
    print(yellow('============================',bold=True))
    print()    
    current_firewall_ip_blocking_list=[]
    SecureX_Current_list=tor_dict # TOR IP list currently in SecureX Judgments
    # connect to the tor ip list
    print()
    print(cyan("- connect to https://check.torproject.org/torbulkexitlist and get the current IP list",bold=True))
    print()
    resp = requests.get('https://check.torproject.org/torbulkexitlist')
    ip_list=''
    nb_added=0
    nb_removed=0
    #print(resp.status_code)
    #sys.exit() # uncomment if you need to troubleshoot
    if resp.status_code==200:
        print(green("--> OK done",bold=True))
        print()    
        final_result_txt='' # create a text variable for receiving urls
        ip_list=resp.text
        temp_list=ip_list.split('\n')
        nb=len(temp_list)
        # Let's put result into a text file which is easier to manage
        for item in temp_list:
            if item not in current_firewall_ip_blocking_list:
                nb_added+=1
                if len(item.strip()):
                    current_firewall_ip_blocking_list.append(item) 
        # Let's put result into a text file which is easier to manage = DONE
        # Let's go thru to last TOR list and remove from Judgement IP addresses that disapeared
        for item in SecureX_Current_list:
            if item not in temp_list:
                item_id=SecureX_Current_list[item]
                info='--- REMOVE from SecureX Judgements: '+item+' : ID = '+item_id
                response = requests.delete(item_id, headers=headers)
                print(red(info,bold=True))
                #print(yellow(resp.status_code,bold=True))
                if resp.status_code!=200:
                    print(red("---- Error - couldn't remove entry",bold=True))
                    if response.status_code==401:   
                        print(red('ask again for a token'))
                        access_token=get_token()
                        headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
                        response = requests.delete(item_id, headers=headers)     
                        if resp.status_code!=200:
                            print(red("---- Error - couldn't remove entry",bold=True))           
                        else:
                            print(green("---- Success - entry removed",bold=True))                            
                else:
                    print(green("---- Success - entry removed",bold=True))
            else:
                info=item+'--- Keep this one in the SecureX Judgements: '
                print(green(info,bold=True)) 
        print(yellow('new step : get indicator list',bold=True))
        indicator_list=get_indicators(access_token)
        print(green(indicator_list,bold=True))                
        print('indicator_list :',cyan(indicator_list,bold=True))
        print()
        indicator_id=indicator_list[1]['Secure_Firewall_SecureX_Indicator_IPv4']  
        # Let's go thru to last TOR list and remove from Judgement IP addresses that disapeared and add new IP addresses into Judgments        
        for item in temp_list:
            if item not in SecureX_Current_list:
                info='---   Add this new IP to SecureX Judgments : '+item
                judgment_id=add_secureX_judgment_for_this_ip(access_token,item)
                print(cyan(info,bold=True))
                print('resulting judgement id :',cyan(judgment_id,bold=True))
                print(yellow('new step : create relationship',bold=True))
                create_relationship_for_feed(access_token,judgment_id,indicator_id,item)
                
    return 1
    
def main():
    access_token=get_token()
    print(yellow('New step : Create new judgment for IP',bold=True))
    tor_ip_list_in_SecureX_Judgments=get_judgments(access_token)
    payload = json.dumps(tor_ip_list_in_SecureX_Judgments,indent=4,sort_keys=True, separators=(',', ': '))
    print()
    print(cyan(payload,bold=True))
    print()
    # get_last_tor_blocking_list and update SecureX judgments and feeds
    current_tor_list=get_last_tor_blocking_list(tor_ip_list_in_SecureX_Judgments)
    
if __name__ == "__main__":
    main()
