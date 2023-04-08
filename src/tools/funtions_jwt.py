from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

import ENVS


def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)},
                   key=ENVS.SECRET_KEY_TOKEN, algorithm="HS256")
    return token.encode("UTF-8")


def validate_token(token):
    try:
        return {"message": "Valid Token", "status": decode(token, key=ENVS.SECRET_KEY_TOKEN, algorithms=["HS256"])}
    except exceptions.DecodeError:
        response = {"message": "Invalid Token"}
        return response
    except exceptions.ExpiredSignatureError:
        response = {"message": "Token Expired"}
        return response