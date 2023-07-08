# External Packages
from flask import Blueprint, request
from flask import render_template
import json
import requests
import config.base as CONFIG

from tools.functions_authentication import valid_headers

from ..views.service import register_service_route_POST

views_services = Blueprint("services", __name__)


@views_services.route("/api/v1/register_service", methods=["POST"])
def register_service():
    """SignUp EndPoint

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

    api_key=request.headers.get("Api-Key")

    if api_key != CONFIG.API_KEY:
        response = {
            "Success": False,
            "Message": "Not API_KEY Valid",
            "Data": {},
        }

        return response

    if request.method == "POST":
        response = register_service_route_POST(parameters_json=request.get_json())
        return response