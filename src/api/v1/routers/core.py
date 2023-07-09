# External Packages
from flask import Blueprint, request
from http import HTTPStatus

#Local Packages
import config.base as CONFIG
from tools.functions_authentication import valid_headers

from ..views.core import signin_route_PUT, validate_token_route_GET

#Definition of Views
views_core = Blueprint("core", __name__)


@views_core.route("/", methods=["GET"])
def index():
    """Respond with the API documentation

    Returns:
        str: API Documentation
    """
    api_docs = open(f"templates/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()


@views_core.route("/api/v1/signin", methods=["PUT"])
def signin():
    """SignIn Route

    Returns:
        tuple: tuple of Dict and HTTP Code exmaple
        {
            "Data": {
                .
                .
                .
            },
            "Message": "....",
            "Success": true
        }
    """
    response_credentials, status_code = valid_headers(request)
    if not response_credentials.get("Success"):
        return response_credentials, status_code

    if request.method == "PUT":
        response = signin_route_PUT(request=request)
        return response


@views_core.route("/test", methods=["GET"])
def test():
    """Test Route

    Returns:
        str: simple str
    """
    return "Hello World!!!"

@views_core.route("/api/v1/development/users", methods=["GET"])
def development_get_users():
    """Test Route

    Returns:
        str: simple str
    """

    api_key=request.headers.get("Api-Key")

    if api_key != CONFIG.API_KEY:
        response = {
            "Success": False,
            "Message": "Not API_KEY Valid",
            "Data": {},
        }

        return response

    from config.database import get_session
    from models import UsersModel
    session = get_session()
    users = (
        session.query(UsersModel).all()
    )
    session.close()

    # Convertir la lista de objetos SQLAlchemy a una lista de diccionarios JSON
    users_json = []

    for user in users:
        users_json.append(user.toJSON())
    
    response = {
        "Success": True,
        "Message": "Success Get Users",
        "Data":   users_json,
    }
    return response, HTTPStatus.CREATED

@views_core.route("/api/v1/development/services", methods=["GET"])
def development_get_services():
    """Test Route

    Returns:
        str: simple str
    """

    api_key=request.headers.get("Api-Key")

    if api_key != CONFIG.API_KEY:
        response = {
            "Success": False,
            "Message": "Not API_KEY Valid",
            "Data": {},
        }

        return response

    from config.database import get_session
    from models import ServicesModel
    import json
    from datetime import datetime
    session = get_session()
    services = (
        session.query(ServicesModel).all()
    )
    session.close()

    # Convertir la lista de objetos SQLAlchemy a una lista de diccionarios JSON
    services_json = []

    for service in services:
        services_json.append(service.toJSON())
    
    response = {
        "Success": True,
        "Message": "Success Get Services",
        "Data":   services_json,
    }
    return response, HTTPStatus.CREATED