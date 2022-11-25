'''
    Create a bundle incident + sightings + relationship
'''
import requests
import json
from crayons import *
from datetime import datetime, timedelta
import time
import sys

host = "https://private.intel.eu.amp.cisco.com"
item_list=[]

discover_method=["Agent Disclosure","Antivirus","Audit","Customer","External - Fraud Detection","Financial Audit","HIPS","IT Audit","Incident Response","Internal - Fraud Detection","Law Enforcement"]

categories=["Denial of Service","Exercise/Network Defense Testing","Improper Usage","Investigation","Malicious Code","Scans/Probes/Attempted Access","Unauthorized Access"]



def current_date_time():
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return(current_time)
    
def current_date_time_simple():
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    return(current_time)
    
def date_plus_x_days(nb):  
    '''
        working example
    '''
    current_time = datetime.utcnow()
    start_time = current_time + timedelta(days=nb)
    timestampStr = start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return(timestampStr)
    
def create_bunble_json_0():
    sighting_title= "Endpoint Severe Infection"
    source="PATRICK NEW TEST"
    source_uri="https://www.cisco.com/c/en/us/products/security/cyber-vision/index.html"
    relationship_type="member-of"
    source_ref="transient:patrick-sighting-bbcde36fe2c678aa969162272ed8e8ac215f7705b13f4e2530d1c572a9"
    target_ref="transient:patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    sighting_id="patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    sighting_source_uri="https://www.google.com"
    sighting_severity="High"
    sighting_confidence="High"
    sensor='endpoint'
    incident_title="Patrick Endpoint Incident"    
    incident_short_description="This is a short description for this incident"
    time=current_date_time()
    incident_description=f"| Incident title |PATRICK INCIDENT |\n| -------- |-------- |\n| Event time |{time} |\n| Promoted at |{time}  |\n| Promoted by |pcardot@cisco.com (PATRICK NEW Cardot) |\n| Promotion reason |demo data |\n| Reporting device type |PATRICK NEW TEST Center |\n| Event details |https://Center/v2/#/events/ |\n"
    incident_source_uri='https://www.google.com'
    incident_confidence="High"
    target='endpoint'
    discovery_method="Automated detection by Secure Endpoint"
    promotion_method="Automated" # Manual or Automated
    # Here under the JSON data
    json_data={"type":"bundle",
    "source":source,
    "source_uri":source_uri,
    "relationships":[
        {
            "type":"relationship",
            "source":source,
            "source_uri":source_uri,
            "relationship_type":relationship_type,
            "source_ref":source_ref,
            "target_ref":target_ref
        }
        ],
    "sightings":[
            {
                "id":source_ref,
                "title": sighting_title,
                "type":"sighting",
                "external_ids":[source_ref],
                "source":source,
                "source_uri":sighting_source_uri,
                "severity":sighting_severity,
                "confidence":sighting_confidence,
                "observed_time":
                    {"start_time":current_date_time()},
                "sensor":sensor,
                "sensor_coordinates":{
                    "type":sensor,
                    "observables":[
                                {"type":"ip","value":"192.168.69.22"},
                                {"type":"device","value":"FCH2307Y036"}
                        ]
                    },
                "observables":[
                        {"type":"ip","value":"13.67.68.224"}
                    ],
                "relations":[
                        {"source":{"type":"ip","value":"13.67.68.224"},"related":{"type":"ip","value":"10.0.0.76"},"relation":"Connected_To","origin":"Sensor XYZ "}
                    ],
                "targets":[
                    {"type":target,
                    "observables":[
                        {"type":"ip","value":"10.0.0.76"}
                        ],
                        "observed_time":
                        {"start_time":current_date_time()}
                    }
                ]
            }
        ],
    "incidents":[
            {"id":target_ref,
            "type":"incident",
            "external_ids":[target_ref],
            "source":source,
            "source_uri":incident_source_uri,
            "title":incident_title,
            "short_description":incident_short_description,
            "description":incident_description,
            "confidence":incident_confidence,
            "status":"New",
            "incident_time":{"opened":current_date_time(),"discovered":current_date_time()},
            "categories":[categories[3]],
            "discovery_method":discover_method[2],
            "promotion_method":promotion_method
            }
        ]
    }
    return(json_data)

def create_bunble_json():
    '''
        create an incident + sighting and dynamically create the JSON payload
    '''
    # Bundle global
    source_ref="transient:patrick-sighting-bbcde36fe2c678aa969162272ed8e8ac215f7705b13f4e2530d1c572a9"
    target_ref="transient:patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    # Incident definition
    incident_severity="Critical"    
    incident_short_description="Infection example for PVT Lab"
    time=current_date_time_simple()
    incident_title="PVT Endpoint Infection demo"    
    incident_description=f"| Incident Title | LAPTOP SEVERE INFECTION |\n| - | - |\n| Promoted at | {time} UTC |\n| Promotion method | Automated |\n| Indicators | **Possible Powershell Post-Exploitation Loader**: Several PowerShell-based post exploitation frameworks such as PowerShell Empire and CobaltStrike loaders decode and run byte code in memory, which is often also compressed and base64-encoded. A PowerShell command similar to such frameworks was executed. |\n| MITRE Tactics | [TA0005](https://attack.mitre.org/tactics/TA0005): Defense Evasion<br>[TA0002](https://attack.mitre.org/tactics/TA0002): Execution |\n| MITRE Techniques | [T1059.001](https://attack.mitre.org/techniques/T1059/001): PowerShell |\n| Host name | Patrick_Laptop |\n| GUID | 57150e86-fcbe-47ff-8bc7-3f297d473b79 |\n| Operating System | Windows 8.1 Connected (Build 9600.19893) |\n| Group | Patrick_Group |\n| Policy | Audit_Patrick |\n| Internal IP | 192.168.128.137 |\n| External IP | 10.0.0.76 |\n"
    incident_source_uri='https://console.eu.amp.cisco.com/computers/57150e86-fcbe-47ff-8bc7-3f297d473b79/trajectory2'
    incident_confidence="High"   
    discovery_method="Automated detection by Secure Endpoint"
    promotion_method="Automated" # Manual or Automated    
    #Sighting Definition
    sighting_title= "Endpoint Severe Infection"
    source="PATRICK NEW TEST"
    source_uri="https://www.cisco.com/c/en/us/products/security/cyber-vision/index.html"
    relationship_type="member-of"
    sighting_id="patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    sighting_source_uri="https://www.google.com"
    sighting_severity="High"
    sighting_confidence="High"
    sensor='endpoint'    
    target='endpoint'
    #//////////////////////////////

    # Here under the JSON data
    json_data={"type":"bundle",
    "source":source,
    "source_uri":source_uri,
    "relationships":[
        {
            "type":"relationship",
            "source":source,
            "source_uri":source_uri,
            "relationship_type":relationship_type,
            "source_ref":source_ref,
            "target_ref":target_ref
        },
        {
            "type":"relationship",
            "source":source,
            "source_uri":source_uri,
            "relationship_type":relationship_type,
            "source_ref":"https://private.intel.eu.amp.cisco.com:443/ctia/sighting/sighting-3abcc481-c795-49fe-965e-7f0f6ce68e8e",
            "target_ref":target_ref
        }        
        ],
    "sightings":[
            {
                "id":source_ref,
                "title": sighting_title,
                "type":"sighting",
                "external_ids":[source_ref],
                "source":source,
                "source_uri":sighting_source_uri,
                "severity":sighting_severity,
                "confidence":sighting_confidence,
                "observed_time":
                    {"start_time":current_date_time()},
                "sensor":sensor,
                "sensor_coordinates":{
                    "type":sensor,
                    "observables":[
                                {"type":"ip","value":"192.168.69.22"},
                                {"type":"device","value":"Example of Devide Identifier"}
                        ]
                    },
                "observables":[
                        {"type":"ip","value":"13.67.68.224"}
                    ],
                "relations":[
                        {"source":{"type":"ip","value":"13.67.68.224"},"related":{"type":"ip","value":"10.0.0.76"},"relation":"Connected_To","origin":"Sensor XYZ"}
                    ],
                "targets":[
                    {"type":target,
                    "observables":[
                        {"type":"ip","value":"10.0.0.76"}
                        ],
                        "observed_time":
                        {"start_time":current_date_time()}
                    }
                ]
            },
            {                
                "id":"https://private.intel.eu.amp.cisco.com:443/ctia/sighting/sighting-3abcc481-c795-49fe-965e-7f0f6ce68e8e",
                "title": "Possible Powershell Post-Exploitation Loader",
                "type":"sighting",
                "external_ids":["https://private.intel.eu.amp.cisco.com:443/ctia/sighting/sighting-3abcc481-c795-49fe-965e-7f0f6ce68e8e"],
                "source":"Secure Enpoint",
                "source_uri":"https://console.eu.amp.cisco.com/computers/57150e86-fcbe-47ff-8bc7-3f297d473b79/trajectory2?_ts=1669279034647&id=7169498858928483382",
                "severity":"Critical",
                "confidence":"High",
                "observed_time":
                    {"start_time":current_date_time()},
                "sensor":"endpoint",
                "sensor_coordinates":{
                    "type":"endpoint",
                    "observables":[
                                {"type":"ip","value":"192.168.69.22"},
                                {"type":"device","value":"Example of Devide Identifier"}
                        ]
                    },
                "observables":[
                        {"type":"sha256","value":"6f88fb88ffb0f1d5465c2826e5b4f523598b1b8378377c8378ffebc171bad18b"},
                        {"type":"sha256","value":"840e1f9dc5a29bebf01626822d7390251e9cf05bb3560ba7b68bdb8a41cf08e3"}
                    ],
                "targets":[
                    {"type":"endpoint",
                    "observables":[
                        {"type":"ip","value":"10.0.0.76"},
                        {"type":"hostname","value":"Victim Endpoint"},
                        {"type":"amp_computer_guid","value":"57150e86-fcbe-47ff-8bc7-3f297d473b79"},
                        {"type":"hostname","value":"Victim Endpoint"},
                        {"type":"ip","value":"192.168.128.137"}
                        ],
                        "observed_time":
                        {"start_time":current_date_time()}
                    }
                ]
            }           
        ],
    "incidents":[
            {"id":target_ref,
            "type":"incident",
            "external_ids":[target_ref],
            "source":source,
            "source_uri":incident_source_uri,
            "title":incident_title,
            "short_description":incident_short_description,
            "description":incident_description,
            "confidence":incident_confidence,
            "severity":incident_severity,
            "status":"New",
            "incident_time":{"opened":current_date_time(),"discovered":current_date_time()},
            "categories":[categories[3]],
            "discovery_method":discover_method[2],
            "promotion_method":promotion_method
            }
        ]
    }
    return(json_data)
    
def create_event_bunble_json():
    '''
        create the incident with a sighthing
    '''
    # Bundle global
    source_ref="transient:patrick-sighting-bbcde36fe2c678aa969162272ed8e8ac215f7705b13f4e2530d1c572a9"
    target_ref="transient:patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    # Incident definition
    incident_severity="Critical"    
    incident_short_description="Infection example for PVT Lab"
    time=current_date_time_simple()
    incident_title="PVT Endpoint Infection demo"    
    incident_description=f"| Incident Title | LAPTOP SEVERE INFECTION |\n| - | - |\n| Promoted at | {time} UTC |\n| Promotion method | Automated |\n| Indicators | **Possible Powershell Post-Exploitation Loader**: Several PowerShell-based post exploitation frameworks such as PowerShell Empire and CobaltStrike loaders decode and run byte code in memory, which is often also compressed and base64-encoded. A PowerShell command similar to such frameworks was executed. |\n| MITRE Tactics | [TA0005](https://attack.mitre.org/tactics/TA0005): Defense Evasion<br>[TA0002](https://attack.mitre.org/tactics/TA0002): Execution |\n| MITRE Techniques | [T1059.001](https://attack.mitre.org/techniques/T1059/001): PowerShell |\n| Host name | Patrick_Laptop |\n| GUID | 57150e86-fcbe-47ff-8bc7-3f297d473b79 |\n| Operating System | Windows 8.1 Connected (Build 9600.19893) |\n| Group | Patrick_Group |\n| Policy | Audit_Patrick |\n| Internal IP | 192.168.128.137 |\n| External IP | 10.0.0.76 |\n"
    incident_source_uri='https://console.eu.amp.cisco.com/computers/57150e86-fcbe-47ff-8bc7-3f297d473b79/trajectory2'
    incident_confidence="High"   
    discovery_method="Automated detection by Secure Endpoint"
    promotion_method="Automated" # Manual or Automated    
    #Sighting Definition
    sighting_title= "Endpoint Severe Infection"
    source="PATRICK NEW TEST"
    source_uri="https://www.cisco.com/c/en/us/products/security/cyber-vision/index.html"
    relationship_type="member-of"
    sighting_id="patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    sighting_source_uri="https://www.google.com"
    sighting_severity="High"
    sighting_confidence="High"
    sensor='endpoint'    
    target='endpoint'
    #//////////////////////////////

    # Here under the JSON data
    json_data={"type":"bundle",
    "source":source,
    "source_uri":source_uri,
    "relationships":[
        {
            "type":"relationship",
            "source":source,
            "source_uri":source_uri,
            "relationship_type":relationship_type,
            "source_ref":source_ref,
            "target_ref":target_ref
        }      
        ],
    "sightings":[
            {
                "id":source_ref,
                "title": sighting_title,
                "type":"sighting",
                "external_ids":[source_ref],
                "source":source,
                "source_uri":sighting_source_uri,
                "severity":sighting_severity,
                "confidence":sighting_confidence,
                "observed_time":
                    {"start_time":current_date_time()},
                "sensor":sensor,
                "sensor_coordinates":{
                    "type":sensor,
                    "observables":[
                                {"type":"ip","value":"192.168.69.22"},
                                {"type":"device","value":"Example of Devide Identifier"}
                        ]
                    },
                "observables":[
                        {"type":"ip","value":"13.67.68.224"}
                    ],
                "relations":[
                        {"source":{"type":"ip","value":"13.67.68.224"},"related":{"type":"ip","value":"10.0.0.76"},"relation":"Connected_To","origin":"Sensor XYZ"}
                    ],
                "targets":[
                    {"type":target,
                    "observables":[
                        {"type":"ip","value":"10.0.0.76"}
                        ],
                        "observed_time":
                        {"start_time":current_date_time()}
                    }
                ]
            }          
        ],
    "incidents":[
            {"id":target_ref,
            "type":"incident",
            "external_ids":[target_ref],
            "source":source,
            "source_uri":incident_source_uri,
            "title":incident_title,
            "short_description":incident_short_description,
            "description":incident_description,
            "confidence":incident_confidence,
            "severity":incident_severity,
            "status":"New",
            "incident_time":{"opened":current_date_time(),"discovered":current_date_time()},
            "categories":[categories[3]],
            "discovery_method":discover_method[2],
            "promotion_method":promotion_method
            }
        ]
    }
    return(json_data)
    
def add_sighting_to_incident_bunble_json():
    '''
        add a sighthing to the existing incident
    '''
    # Bundle global
    source_ref="transient:patrick-sighting-aacde36fe2c678aa969162272ed8e8ac215f7705b13f4e2530d1c572a9"
    target_ref="transient:patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    # Incident definition
    incident_severity="Critical"    
    incident_short_description="Infection example for PVT Lab"
    time=current_date_time_simple()
    incident_title="PVT Endpoint Infection demo"    
    incident_description=f""
    incident_source_uri='https://console.eu.amp.cisco.com/computers/57150e86-fcbe-47ff-8bc7-3f297d473b79/trajectory2'
    incident_confidence="High"   
    discovery_method="Automated detection by Secure Endpoint"
    promotion_method="Automated" # Manual or Automated    
    #Sighting Definition
    sighting_title= "Possible Powershell Post-Exploitation Loader"
    source="PATRICK NEW TEST"
    source_uri="https://www.cisco.com/c/en/us/products/security/cyber-vision/index.html"
    relationship_type="member-of"
    sighting_id="patrick-incident-bbcde9024ffecb353db95ce9cbce57ce7c7de01358a5e39c5950d8fbafe"
    sighting_source_uri="https://www.google.com"
    sighting_severity="High"
    sighting_confidence="High"
    sensor='endpoint'    
    target='endpoint'
    #//////////////////////////////

    # Here under the JSON data
    json_data={"type":"bundle",
    "source":source,
    "source_uri":source_uri,
    "relationships":[
        {
            "type":"relationship",
            "source":source,
            "source_uri":source_uri,
            "relationship_type":relationship_type,
            "source_ref":source_ref,
            "target_ref":target_ref
        }      
        ],
    "sightings":[
            {                
                "id":source_ref,
                "title": sighting_title,
                "type":"sighting",
                "external_ids":[source_ref],
                "source":source,
                "source_uri":"https://console.eu.amp.cisco.com/computers/57150e86-fcbe-47ff-8bc7-3f297d473b79/trajectory2?_ts=1669279034647&id=7169498858928483382",
                "severity":"High",
                "confidence":"High",
                "observed_time":
                    {"start_time":current_date_time()},
                "sensor":"endpoint",
                "sensor_coordinates":{
                    "type":"endpoint",
                    "observables":[
                                {"type":"ip","value":"192.168.69.22"},
                                {"type":"device","value":"Example of Devide Identifier"}
                        ]
                    },
                "observables":[
                        {"type":"sha256","value":"6f88fb88ffb0f1d5465c2826e5b4f523598b1b8378377c8378ffebc171bad18b"},
                        {"type":"sha256","value":"840e1f9dc5a29bebf01626822d7390251e9cf05bb3560ba7b68bdb8a41cf08e3"}
                    ],
                "targets":[
                    {"type":"endpoint",
                    "observables":[
                        {"type":"ip","value":"10.0.0.76"},
                        {"type":"hostname","value":"Victim Endpoint"},
                        {"type":"amp_computer_guid","value":"57150e86-fcbe-47ff-8bc7-3f297d473b79"},
                        {"type":"hostname","value":"Victim Endpoint"},
                        {"type":"ip","value":"192.168.128.137"}
                        ],
                        "observed_time":
                        {"start_time":current_date_time()}
                    }
                ]
            }           
        ],
    "incidents":[
            {"id":target_ref,
            "type":"incident",
            "external_ids":[target_ref],
            "source":source,
            "source_uri":incident_source_uri,
            "title":incident_title,
            "incident_time":{"opened":current_date_time(),"discovered":current_date_time()},
            "confidence":incident_confidence,
            "severity":incident_severity,
            "status":"New",
            "incident_time":{"opened":current_date_time(),"discovered":current_date_time()},
            "categories":[categories[3]],
            "discovery_method":discover_method[2],
            "promotion_method":promotion_method            
            }
        ]
    }
    return(json_data)
    
def create_bundle(host,access_token):
    '''
        open the incident-2.json file which is a bundle definition ( new incident + sighting ) and create an incident
    '''
    with(open("incident-2.json","r")) as file:
        incident_txt=file.read()
    incident_json=json.loads(incident_txt)
    print(incident_json)
    print()
    print("Let's connect to CTIA and create the incident")
    print()
    url = f"{host}/ctia/bundle/import" 
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=incident_json,headers=headers)
    print()
    print("Ok Done")
    print()    
    print(response)
    return 1
    
def create_bundle_dynamic_json(host,access_token):
    '''
        create a bundle JSON payload ( incident + sighthings ) and create the incident
    '''
    incident_json=create_bunble_json()
    '''
    print()   
    print(yellow(type(incident_txt),bold=True))
    print()    
    incident_json=json.loads(incident_txt)
    '''
    print()
    print(incident_json)
    print()
    #sys.exit()
    print("Let's connect to CTIA and create the incident")
    print()
    url = f"{host}/ctia/bundle/import" 
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=incident_json,headers=headers)
    print()
    print("Ok Done")
    print()    
    print(response)
    print()    
    print(response.json())    
    return 1
    
    
def create_incident_with_sightings(host,access_token):
    '''
        create new incident with one sighting and add a second sigthing into it
    '''
    incident_json=create_event_bunble_json()
    '''
    print()   
    print(yellow(type(incident_txt),bold=True))
    print()    
    incident_json=json.loads(incident_txt)
    '''
    print()
    print(incident_json)
    print()
    #sys.exit()
    print("Let's connect to CTIA for creating the event")
    print()
    url = f"{host}/ctia/bundle/import" 
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=incident_json,headers=headers)
    print()
    print("Ok Done")
    print()    
    print(response)
    print()    
    print(response.json())    
    GO=input("Ok Next Step :")
    print()
    print("Now let's add another sighting to the incident")
    print()      
    incident_json=add_sighting_to_incident_bunble_json()
    '''
    print()   
    print(yellow(type(incident_txt),bold=True))
    print()    
    incident_json=json.loads(incident_txt)
    '''
    print()
    print(incident_json)
    print()
    #sys.exit()
    print("Let's connect to CTIA for creating the event")
    print()
    url = f"{host}/ctia/bundle/import" 
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=incident_json,headers=headers)
    print()
    print("Ok Done")
    print()    
    print(response)
    print()    
    print(response.json())  
    
    return 1
    
def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    #create_bundle(host,access_token)  # test 1
    #create_bundle_dynamic_json(host,access_token) # test 2
    create_incident_with_sightings(host,access_token) # test 3


if __name__ == "__main__":
    main()
