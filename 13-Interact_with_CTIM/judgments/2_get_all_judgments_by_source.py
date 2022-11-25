'''
 Get all judgements in your private intelligence from a specific source ( see source_to_select variable line 11 )
 
 and store results into output text files
'''
import requests
import json
from crayons import *

host = "https://private.intel.eu.amp.cisco.com"
item_list=[]

source_to_select="source.example.org"  # exact source name to filter
source_to_select="Patrick"

def get(host,access_token,url,offset,limit):    
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    url = f"{host}{url}?limit={limit}&offset={offset}"
    response = requests.get(url, headers=headers)
    return response

def get_judgments(access_token):
    fb = open("z_json_judgements_list.json", "w")
    fd = open("z_judgements_id_list.txt", "w")
    json_output='[\n'
    fc = open("z_judgment_list.txt", "w")
    url = "/ctia/judgement/search"
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
            if item['source']==source_to_select:
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
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    get_judgments(access_token)

if __name__ == "__main__":
    main()
