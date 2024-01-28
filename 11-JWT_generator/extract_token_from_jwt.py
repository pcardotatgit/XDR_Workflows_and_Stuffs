from authlib.jose import jwt
from authlib.jose.errors import BadSignatureError, DecodeError
from flask import current_app, jsonify, request
from datetime import datetime, timedelta
from crayons import *
from errors import AuthorizationError, InvalidArgumentError

SECRET ="UFGxYcMj0Om8QKblKzlS2ifurNnSNFGIPuUCGcr9dUzU2TAyJtAUEEvHiKLIuDpt"
JWT="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiIxMjM0NTY3ODkwMjM0NTY3ODk4OTAyMzQ1Njc4OTAyMzQ1Njc4OTAifQ.8dE8sYYFShJ4nfQCIeNNpZHAOv5BruqSU_CpuzlJb64"
source="NO XDR Call but static JWT"

def get_auth_token():
    """
    Parse and validate incoming request Authorization header.

    NOTE. This function is just an example of how one can read and check
    anything before passing to an API endpoint, and thus it may be modified in
    any way, replaced by another function, or even removed from the module.
    """
    expected_errors = {
        KeyError: 'Authorization header is missing',
        AssertionError: 'Wrong authorization type'
    }    
    if source=="XDR Call":
        # This if branch is an example from CiscoSecuritygithub relay modules that read the JWT sent by XDR
        scheme, token = request.headers['Authorization'].split()
        assert scheme.lower() == 'bearer'
        return token
    else:
        # in this branch we use the JWT variable value as an example
        return JWT

def get_jwt():
    """
    Parse the incoming request's Authorization Bearer JWT for some credentials.
    Validate its signature against the application's secret key.

    NOTE. This function is just an example of how one can read and check
    anything before passing to an API endpoint, and thus it may be modified in
    any way, replaced by another function, or even removed from the module.
    """
    expected_errors = {
        KeyError: 'Wrong JWT payload structure',
        TypeError: '<SECRET_KEY> is missing',
        BadSignatureError: 'Failed to decode JWT with provided key',
        DecodeError: 'Wrong JWT structure'
    }    
    token = get_auth_token()
    print(cyan(f'Received JWT = {token}',bold=True))  
    try:     
        result=(jwt.decode(token, SECRET)['key'])
        print(red(f'3rd party token : {result}',bold=True))      
        return result
    except tuple(expected_errors) as error:
        print()
        print(red(f'WRONG DATA INTO THE JWT - PROBABLY WRONG SECRET !',bold=True))
        print()
        raise AuthorizationError(expected_errors[error.__class__])    


if __name__=="__main__":
    token=get_jwt()
    print(yellow("the original token is :",bold=True))
    print(yellow(token,bold=True))
    