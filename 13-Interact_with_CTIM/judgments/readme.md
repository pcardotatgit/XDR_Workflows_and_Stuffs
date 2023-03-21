# Create, read and delete Judgments

The scripts in this repo give you some examples for interacting with judgments in the SecureX private intelligence.

First of all you have to edit the **config.py** file and set the correct values for **ctr_client_id , ctr_client_password, host and host_for_token**

Then you can use the scripts :

- **0-generate_and_save_token.py** : Ask for a Token to SecureX. This is the first thing to do
- **1_get_all_judgments.py** : get all judgments into your private intell and create a few result files **z_json_judgements_list.json, z_judgment_list.txt and z_judgements_id_list.txt**
- **2_get_all_judgments_by_source.txt** : get judgments into your private intell filtered by a key value into the JSON result. And create a few result files **z_json_judgements_list.json, z_judgment_list.txt and z_judgements_id_list.txt**
- **3-delete_judgments.py** : delete all judgments from the **z_judgements_id_list.txt** field.
- **4-create_judgment.py** an example of judgment creation. Result can be check in SecureX at : https://visibility.eu.amp.cisco.com/intelligence/judgements/private
- **5-get_tor_ip_list.py** Collect the IP entry/exit list from check.torproject.org and store the result into a text file ( **create_securex_judgments_from_txt_list.txt**). And loop every xx seconds in order to keep the blocking list updated.
- **6-create_securex_judgments_from_txt_list** : Read the **create_securex_judgments_from_txt_list.txt** and create judgements for all IP addresses into SecureX Judgments ( with no deduplication !)
- **7_keep_tor_ip_addresses_in_judgment_updated.py** - This is an all in one example. This scripts keeps udpated the SecureX Judgements for TOR entry/exit ip addresses. It manages Token requests and expirations, the TOR list download and SecureX Judgement update, with IP addrresses to remove, to keep and to add.
