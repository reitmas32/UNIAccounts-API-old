# Local Packages
from http import HTTPStatus

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from ..schemas import ServiceSchema
from ..services.services import ServicesService


def register_service_route_POST(parameters_json: dict):
    """EndPoint /signup with method HTTP POST, Create new User in DataBase

    Args:
        parameters_json (dict): User data
    Returns:
        dict: response of the operation in the DataBase
    """

    try:
        service_schema = ServiceSchema(**parameters_json)
    except ValidationError as e:
        errors = []
        for error in e.errors():
            errors.append({"field": error["loc"][0], "message": error["msg"]})

        response = {
            "Success": False,
            "Message": "Data invalid for create user",
            "Data": {"errors": errors},
        }
        return response, HTTPStatus.BAD_REQUEST

    service_service = ServicesService()
    try:
        service_model = service_service.create_service(service_data=service_schema)
    except IntegrityError as e:
        response = {
            "Success": False,
            "Message": "Error for create user",
            "Data": {"errors": str(e)},
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    response = {
        "Success": True,
        "Message": "Success signup, user create",
        "Data": {
            "Name": service_model.name,
            "API_KEY": service_model.api_key,
            "jwt_exp": service_model.jwt_exp,
            "mother_login": service_model.mother_login,
        },
    }
    return response, HTTPStatus.CREATED
