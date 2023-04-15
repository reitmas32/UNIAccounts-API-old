######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 06/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# Local Packages
from services.db.idata_base import IDataBase
from models.user import User


def signin_route_PUT(parameters_json: dict, data_base: IDataBase, service_name: str):
    """EndPoint /signin with method HTTP PUT

    Args:
        parameters_json (dict): User data
        data_base (IDataBase): Implementation of the database to be used
        service_name (str): Name of the service requested by the operation

    Returns:
        dict: response of the operation in the DataBase
    """
    new_user = User.from_dict_password_nohash(parameters_json)
    if new_user == None:
        return {'message': 'Error User no created', 'status_code': 428}
    response = data_base.signin_user(new_user, service_name)
    return response


def signin_route_GET(token_authorization: str, data_base: IDataBase, service_name: str):
    """EndPoint /signin with method HTTP GET,  verify that the session 
        corresponding to the token is active 

    Args:
        token_authorization (str): JWT of session
        data_base (IDataBase): Implementation of the database to be used
        service_name (str): Name of the service requested by the operation

    Returns:
        dict: response of the operation in the DataBase
    """
    response = data_base.check_token_user(token_authorization, service_name)
    return response