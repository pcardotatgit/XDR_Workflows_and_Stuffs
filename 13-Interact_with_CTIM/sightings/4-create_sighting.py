'''
    create a sighting into your SecureX private intelligence
'''

import requests
import json
from datetime import datetime, timedelta
import time
from crayons import *
import sys

payload_model = {
  "valid_time": {
    "start_time": "2022-02-05T12:55:08.580Z",
    "end_time": "2022-12-08T14:55:08.586Z"
  },
  "schema_version": "1.1.3",
  "observable": {
    "value": "183.83.98.212",
    "type": "ip"
  },
  "reason_uri": "an URL in a string format (optionnal)",
  "type": "judgement",
  "source": "ex : Patrick Honey Pot", #String with at most 2048 characters
  "disposition": 2,# 1 = Clean, 2 = Malicious 3 = Suspicious 4 = Common, 5 = Unknown
  "reason":"a reason of this judgment like : IP used for QakBot C&C", # String with at most 1024 characters
  "source_uri":"https://www.talosintelligence.com/",
  "disposition_name": "Malicious",# Clean, Malicious , Suspicious ,Common, Unknown
  "priority":90,# between & 100
  '''
  A value 0-100 that determine the priority of a judgement. Curated feeds of black/white lists, for example known good products within your organizations, should use a 95. All automated systems should use a priority of 90, or less. Human judgements should have a priority of 100, so that humans can always override machines.
  '''
  "id":"transient:976191af-21c7-42e0-bceb-79dc28d47834", # an ID
  "severity": "Medium",# Medium, Info, Unknown, None, High, Critical, Low
  "tlp": "red", # white, green, red, amber  TLP stands for Traffic Light Protocol, which indicates precisely how this resource is intended to be shared, replicated, copied, etc.
  "timestamp": "2021-02-05T12:55:08.580Z",
  "confidence": "Medium", # Medium, Info, Unknown, None, High, Low 
}

payload_example = {
  "valid_time": {
    "start_time": "2022-02-05T12:55:08.580Z",
    "end_time": "2022-12-08T14:55:08.586Z"
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
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return(current_time)
    
def date_plus_x_days(nb):   
    current_time = datetime.utcnow()
    start_time = current_time + timedelta(days=nb)
    timestampStr = start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return(timestampStr)

def create_sighting(access_token,payload):
    '''
        static payload : payload_example
    '''
    url = 'https://private.intel.eu.amp.cisco.com/ctia/sighting'
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    payload = json.dumps(payload_example)
    response = requests.post(url, headers=headers, data=payload)
    print()
    print (yellow(response,bold=True))  
    print()
    print(green(response.json(),bold=True))
    
def create_sighting_dynamic_payload(access_token):
    '''
        generate dynamically the JSON payload
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
    "value": "60.60.60.60",
    "type": "ip"
    }
    judgment_json["source"] = "Patrick_Sensor"
    disposition='malicious'
    judgment_json["disposition"] = DISPOSITIONS[disposition][0]
    judgment_json["reason"] = "IP Attacked the honeypot"    
    judgment_json["source_uri"] = "https://www.patrick.com/" 
    judgment_json["disposition_name"] = DISPOSITIONS[disposition][1]   
    judgment_json["severity"] ="Medium"
    judgment_json["tlp"] ="green"
    judgment_json["timestamp"] =start_time
    judgment_json["confidence"] ="Medium"   
    print()
    print(red(judgment_json,bold=True))
    print()
    #sys.exit()
    url = 'https://private.intel.eu.amp.cisco.com/ctia/sighting'
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    payload = json.dumps(payload_example)
    response = requests.post(url, headers=headers, data=judgment_json)
    print()
    print (yellow(response,bold=True))  
    print()
    print(green(response.json(),bold=True))

def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    # create_judgments(access_token,payload_example)  # example with static payload
    create_judgments_dynamic_payload(access_token) # example with dynamic payload creation

if __name__ == "__main__":
    main()