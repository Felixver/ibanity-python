from collections import namedtuple
from ibanity import Ibanity
import requests


def create(authorization_code, code_verifier, redirect_uri, client_id, authorization):
    uri = Ibanity.client.api_schema_ponto["oauth2"]["token"] \

    body = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier
        }

    response = Ibanity.client.post(uri, body, {}, authorization)
    return __create_token_named_tuple__(response)


def create_from_refresh_token(refresh_token, authorization, client_id):
    uri = Ibanity.client.api_schema_ponto["oauth2"]["token"] \

    body = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_token_named_tuple__(response["data"])

def __create_token_named_tuple__(token):
    return namedtuple("Token", token.keys())(**token)
