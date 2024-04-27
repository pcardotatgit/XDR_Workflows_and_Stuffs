# JWT Token generator

This script generates a JWT from a JSON payload. 

## Why do we need this ?

Anytime we want to send sensitive data from a REST client to a REST Server, JSON Web Token help to protect these data thanks to a **secret key** that is sent with the data into the JWT and that the relay module knows and uses to check data integrity. 

The result of JWT "protection" is a cyphered data that can be send by the client to the server.

At the server's side the server is able to extract the payload and check the signature. Then it is able to confirm the origin of the data and that they not have been modified during the transfert between XDR and the relay module.

The REST Server is able to check that no Man In The Middle changed the data between the client and the server.

We use this in the XDR Relay Module development context in order to embed the third party solution API token into a JWT we will use in the XDR integration panel.

Then the token we use within XDR is not the Third party solution token, but a JWT token build on the Third party solution token. That give a way to not store this token in clear into XDR.

## Install python modules

It is a good practice to create a python virtual environment first and work inside it.

This script requires 2 modules : crayons and authlib.

Type the 2 following command lines in order to install these modules

    pip install crayons
    pip install authlib
 
## Run the script ?

- Step 1 : Edit the **payload.json** file and copy and paste the third party solution API token in the key value
- Step 2 : Run the gen_jwt.py file : **python gen_jwt.py**
- Step 3 : copy the JWT that appears into the console and is stored into a file named **JWT.txt**. The Secret Key used is stored into a file named **JWT_SECRET.txt**

Create a valid **payload.json** file as the example bellow

    {
        "key_1": "123456789023456789... third party solution API token here ...890234567890234567890",
        "host":"_anything_",
        "other":" anything else "
    }
    
Don't forget the quotes, the column sign and the commas. The it should be okay.

You can add into this json file as much keys as you want. The JWT can be seen on the server console into the data sent into the HTTP request.

The key names and their values will be retrieved by the server into a dictionnay after having decoded and check the JWT.

Then you can check the JWT content in the online site https://jwt.io/

**Notice** the algorithm used in thise example to secure data is ( 'alg': 'HS256' ). This is not the more secured one. In production it will be relevant to use a more secured one !

## Notice 

In the XDRs content development use the payload.json file as it is. With the key name equal to **key**

But in any other case, you can build any other more complex json payload.  As far this payload format is valid, then the generated JWT will secure your data.

Then you can copy and paste the generated JWT into the **Authorization Bearer** edit box of the **Generic Serverless Relay** integration panel in XDR.

## decode the JWT with a python script 

The **extract_token_from_jwt.py** gives an example of how to decode a JWT thanks to python.

This script requires the **errors.py** script as a resource.

Edit the **extract_token_from_jwt.py** script and give the correct value to the **SECRET** and the **JWT** variables at the top of the script.

Then run the script

    python extract_token_from_jwt.py 

## decode the JWT within your XDR Relay Module

The Relay Module template decode the JWT for you. But you have to give to it a correct **SECRET** value.

You can do it by editing the **config.py** script of the **Multi Purpose relay Module Template** and by updating the **JWT_SECRET** variable.