import requests
import time
import config as conf
import sys

# CTR get token
# - check if token stored into config.py
ctr_client_id=conf.ctr_client_id
ctr_client_password=conf.ctr_client_password

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
        
if __name__=='__main__':
    url = 'https://visibility.eu.amp.cisco.com/iroh/oauth2/token'
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
    payload = {'grant_type':'client_credentials'}
    client_id,client_password=read_api_keys('ctr') 
    print(client_id)
    print(client_password)   
    #sys.exit()
    response = requests.post(url, headers=headers, auth=(client_id, client_password), data=payload)
    #print(response.json())
    reponse_list=response.text.split('","')
    token=reponse_list[0].split('":"')
    print(token[1])
    fa = open("ctr_token.txt", "w")
    fa.write(token[1])
    fa.close()