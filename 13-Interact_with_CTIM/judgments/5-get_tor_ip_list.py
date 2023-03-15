'''
    this script keep an updated list of all IP addresses contained into the TOR entry/exit list ( https://check.torproject.org/torbulkexitlist )
    Every "frequency" seconds the script download the list of IP and store a version of it localy
'''
import requests
import sys
import time
from crayons import *
from datetime import datetime, timedelta

frequency=200 # frequency in seconds (  3600 = 1 hour )

def current_date_time():
    '''
        get current date time in yy-mm-dd-H:M:S:fZ format 
    '''
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return(current_time)
    
def update_tor_blocking_list():
    '''
        Get TOR IP List and store it into a local text file        
    '''  
    print()
    print(yellow('============================',bold=True))
    print()    
    current_firewall_ip_blocking_list=[]
    updated_firewall_ip_blocking_list=[]
    with open('current_firewall_blocking_list.txt','r') as fichier:
        text=fichier.read()    
    current_firewall_ip_blocking_list=text.split('\n')
    log=open('log.txt','a+')
    info=current_date_time()+': get last TOR IP List : \n'
    log.write(info)
    log.write('\n')     
    info=''
    # connect to the tor ip list
    print()
    print(cyan("- connect to https://check.torproject.org/torbulkexitlist and download the IP list",bold=True))
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
        for item in temp_list:
            if item not in current_firewall_ip_blocking_list:
                info=info+'---   ADD : '+item+'\n'
                nb_added+=1
                if len(item.strip()):
                    current_firewall_ip_blocking_list.append(item)     
        for item in current_firewall_ip_blocking_list:
            if item not in temp_list:
                info=info+'---   REMOVE : '+item+'\n'
                nb_removed+=1
            else:
                updated_firewall_ip_blocking_list.append(item)
        result=1
    else:
        result=0
    info=info+'===> '+str(nb)+' IP addresses are contained in the last TOR IP list. '+str(nb_added)+' were added in the firewall blocking list AND '+str(nb_removed)+ ' were removed from this list\n'        
    log.write(info)
    log.close()
    with open('current_firewall_blocking_list.txt','w') as fichier:
        out=''
        for item in updated_firewall_ip_blocking_list:    
            if len(item)>2:
                out=out+item+'\n'
        fichier.write(out)     
    return(result)

    
if __name__ == "__main__":
    go=1
    while go:        
        # body of the loop ...    break it with a ctrl+C    
        result=update_tor_blocking_list()        
        if result!=0:  
            print(yellow(f'   Waiting for next poll in {frequency} seconds ',bold=True))
            print()
            print(yellow('============================',bold=True))
            print()                
            time.sleep(frequency)
        else:
            go=0
            with open('log.txt','a+') as log:
                info=current_date_time()+': Error while trying to get last TOR IP List'
                log.write(info)
                log.write('\n')    
            print(red('ERROR',bold=True))

        
