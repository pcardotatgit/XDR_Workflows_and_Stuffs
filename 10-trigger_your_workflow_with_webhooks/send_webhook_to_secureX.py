import requests

url ="COPY HERE THE WHOLE SECUREX WEBHOOK URL"
headers = {'Content-Type': 'application/json charset-utf-8', 'Accept': 'application/json'}

body_message={'message':'Hello Message sent in the body'}

try:
    response = requests.post(url, headers=headers,data=body_message)
    print(response)
except:
    response.raise_for_status()

print("Webhook SENT to SecureX")