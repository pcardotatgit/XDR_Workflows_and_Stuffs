'''
    delete all judgements from z_judgements_id_list.txt file which contains judgment ids
    
    z_judgements_id_list.txt is created by either 1_get_all_judgments.py or 2_get_all_judgments_by_source.py
'''
import requests
import json
from crayons import cyan,green,red,yellow

#access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example
def delete_judgments(access_token):
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    line_content = []
    with open('z_judgements_id_list.txt') as inputfile:
    	for line in inputfile:
    		line_content.append(line.strip())

    # loop through all urls in z_judgements_id_list.txt ( judgment ids ) and delete them
    for url in line_content:
        #  notice url in z_judgements_id_list.txt are actually the full url with judgment IDs
        print (green(url,bold=True))
        response = requests.delete(url, headers=headers)
        print()
        print (yellow(response,bold=True))  

def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    delete_judgments(access_token)

if __name__ == "__main__":
    main()    