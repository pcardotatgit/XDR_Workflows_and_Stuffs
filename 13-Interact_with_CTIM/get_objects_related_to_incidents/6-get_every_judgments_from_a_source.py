'''
 Get all XDR Demo Judgments in your XDR tenant
'''
import requests
import json
from crayons import *

item_list=[]
source_to_select=["securex-orchestration","Patrick Manually added","XDR Demo"]

def parse_config(text_content):
    text_lines=text_content.split('\n')
    host=""
    for line in text_lines:
        print(green(line,bold=True))
        if '.eu.amp.cisco.com' in line:
            host="https://private.intel.eu.amp.cisco.com"
        elif '.intel.amp.cisco.com' in line:
            host="https://private.intel.amp.cisco.com"
        elif '.apjc.amp.cisco.com' in line:
            host="https://private.intel.apjc.amp.cisco.com"            
    print(yellow(host))
    return host

def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    return response
   
    
def get_judgments(host,access_token,source_to_select):
    fb = open("z_json_judgements_list.json", "w")
    fd = open("z_judgements_id_list.txt", "w")
    json_output='[\n'
    fc = open("z_judgment_list.txt", "w")
    url = f"/ctia/judgement/search"
    offset=0
    limit=1000
    go=1 # used to stop the loop   
    while go:      
        index=0
        response = get(host,access_token,url,offset,limit)
        payload = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
        #print(response.json())    
        items=response.json()
        for item in items: 
            index+=1
            if item['source'] in source_to_select:
                print(yellow(item,bold=True))
                item_list.append(item)
                #fb.write(json.dumps(item))
                #fb.write(',\n')
                json_output+=json.dumps(item)
                json_output+=',\n'
                ip=item['observable']['value']    
                print(red(ip,bold=True))
                fc.write(ip)
                fc.write('\n')   
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
    fc.close()
    fd.close()
    
def main():
    with open('config.txt','r') as file:
        text_content=file.read()
    host = parse_config(text_content)
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    print()
    print("Selected Events : ",cyan(source_to_select,bold=True))
    print()
    get_judgments(host,access_token,source_to_select)

if __name__ == "__main__":
    main()