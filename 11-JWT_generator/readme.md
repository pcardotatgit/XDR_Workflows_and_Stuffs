# JWT Token generator

This script generates a JWT from a JSON payload. 

## Why do we need this ?

Anytimez we want to send sensitive data froma REST client to a REST Server, JSON Web Token helps to cypher the data to send with a secret key that is sent into the JWT. Which allow the REST Server to check that no Man In The Middle changed the data between the client and the server.

We use this in the SecureX Relay Module development context in order to embed the third party solution API token into a JWT we will use in the SecureX integration panel.

Then the token we use within SecureX is not the Third party solution token, but a JWT token build on the Third party solution token.

## How to use it ?

- Step 1 : Modify the payload.json file and copy and paste the third party solution API token in the key value
- Step 2 : Run the gen_jwt.py file
- Step 3 : copy the JWT that appears into the console

Then you can check the JWT content in the online site https://jwt.io/

## Remarks 

In the SecureX content development use the payload.json file as it is ( with the keyn nama = to **key**


But in any other case, you can build any other json paylaod as you want.  As far this payload format is valid, then the generated JWT will secure your data.