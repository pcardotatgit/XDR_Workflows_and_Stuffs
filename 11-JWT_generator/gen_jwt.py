import json
import secrets
import string
import sys
from crayons import *

from authlib.jose import jwt

def generate_secret_key():
    """Generate a random 256-bit (i.e. 64-character) secret key."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(64))

def encode_jwt(payload, secret_key):
    """Encode a JWT with the given payload and secret key."""
    header = {'alg': 'HS256', 'typ': 'JWT'}
    return jwt.encode(header, payload, secret_key, check=False).decode('utf-8')

def main():
    secret_key = generate_secret_key()
    print()
    print(white('Secret Key is :',bold=True))
    print(cyan(secret_key,bold=True))
    with open('JWT_SECRET.txt','w') as file:
        file.write(secret_key)
    with open('payload.json','r') as file:
        text_payload=file.read()
    json_payload=json.loads(text_payload) 
    print()    
    print(yellow(f' payload.json : {json_payload}'))
    jwt = encode_jwt(json_payload, secret_key)
    with open('JWT.txt','w') as file:
        file.write(jwt)    
    print()
    print(white('JWT :',bold=True))
    print(cyan(jwt,bold=True))

if __name__ == '__main__':
    main()
