'''
    read the ip_blocking_list.txt file which contain a list of IP addresses, and create SecureX Judgments into SecureX private intelligence
'''
import requests
import sys
import json
import time
from crayons import *
from datetime import datetime, timedelta
import config as conf

host=conf.host

payload_example = {
  "valid_time": {
    "start_time": "2023-03-15T16:32:01.250Z",
    "end_time": "2023-04-14T16:32:01.250Z"
  },
  "schema_version": "1.1.3",
  "observable": {
    "value": "192.241.226.164",
    "type": "ip"
  },
  "reason_uri": "string",
  "type": "judgement",
  "source": "Patrick_Sensor",
  "disposition": 2,
  "reason":"IP Attacked the honeypot",
  "source_uri":"https://www.patrick.com/",
  "disposition_name": "Malicious",
  "priority":90,
  "severity": "Medium",
  "tlp": "green",
  "timestamp": "2022-02-05T12:55:08.580Z",
  "confidence": "Medium"
}

DISPOSITIONS = {
    'clean': (1, 'Clean'),
    'malicious': (2, 'Malicious'),
    'suspicious': (3, 'Suspicious'),
    'common': (4, 'Common'),
    'unknown': (5, 'Unknown')
}

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
    print()
    print(cyan(judgment_json,bold=True))
    print()
    #sys.exit()
    url = f'{host}/ctia/judgement'
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    payload = json.dumps(judgment_json)
    response = requests.post(url, headers=headers, data=payload)
    print()
    print (yellow(response,bold=True))  
    print()
    print(green(response.json(),bold=True))
    
def create_judgments(max_lines:int):
    '''
        read the current_firewall_blocking_list.txt file line by line and create a SecureX Judgment for every ip adresses
        Read only the first max_lines lines
    '''
    with open('current_firewall_blocking_list.txt','r') as fichier:
        text=fichier.read() 
    blocking_list=text.split('\n')
    i=0
    for ip in blocking_list:
        print(cyan(ip,bold=True))
        add_secureX_judgment_for_this_ip(access_token,ip)# add this IP into SecureX judgments
        i+=1
        if i>=max_lines:
            break

if __name__=="__main__":
    print("GO")
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close() 
    nb_of_ip_to_add=100 # limit the number of IP to add in SecureX Judgments
    create_judgments(nb_of_ip_to_add)
    print()
    print(f"DONE - open your brower to : {host}/intelligence/judgements/private  in order to check the result")
    