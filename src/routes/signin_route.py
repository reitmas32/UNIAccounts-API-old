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
    new_user = User.from_dict_password_nohash(parameters_json)
    if new_user == None:
        return {'message': 'Error User no created', 'status_code': 428}
    response = data_base.signin_user(new_user, service_name)
    return response


def signin_route_GET(token_authorization, data_base: IDataBase, service_name: str):
    response = data_base.check_token_user(token_authorization)
    return {'message': response.get('message'), 'status_code': response.get('status_code')}