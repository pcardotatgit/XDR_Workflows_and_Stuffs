# JWT Token generator

This script generates a JWT from a JSON payload. 

## Why do we need this ?

Anytime we want to send sensitive data from a REST client to a REST Server, JSON Web Token help to cypher these data thanks to a **secret key** that is sent with the data into the JWT. 

The result of JWT "protection" is a cyphered data that can be send by the client to the server.

At the server's side the server is able to extract the payload and check the signature. Then is is able to confirm the origin of the data and that they not have been modified during the transfert.

The REST Server is able to check that no Man In The Middle changed the data between the client and the server.

We use this in the XDR Relay Module development context in order to embed the third party solution API token into a JWT we will use in the XDR integration panel.

Then the token we use within XDR is not the Third party solution token, but a JWT token build on the Third party solution token. That give a way to not store this token in clear into XDR.

## How to use it ?

- Step 1 : Modify the payload.json file and copy and paste the third party solution API token in the key value
- Step 2 : Run the gen_jwt.py file
- Step 3 : copy the JWT that appears into the console

Then you can check the JWT content in the online site https://jwt.io/

**Notice** the algorithm used in thise example to secure data is ( 'alg': 'HS256' ). This is not the more secured one. In production it will be relevant to use a more secured one !

## Remarks 

In the XDRs content development use the payload.json file as it is. With the key name equal to **key**

But in any other case, you can build any other more complex json payload.  As far this payload format is valid, then the generated JWT will secure your data.

## decode the JWT with python

The **extract_token_from_jwt.py** gives an example of how to decode a JWT thanks to python.

This script requires the **errors.py** script as a resource.