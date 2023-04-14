from services.db.idata_base import IDataBase
from models.user import User
from tools.funtions_jwt import validate_token


def signin_route_PUT(parameters_json: dict, data_base: IDataBase, service_name: str):
    new_user = User.from_dict_password_nohash(parameters_json)
    if new_user == None:
        return {'message': 'Error User no created', 'status_code': 428}
    response = data_base.find_user(new_user, service_name)
    response = {'message': response.get('message'), 'status_code': response.get('status_code'), 'jwt': response.get('jwt')}
    return response


def signin_route_GET(token_authorization, data_base: IDataBase):
    response = data_base.check_token_user(token_authorization)
    return {'message': response.get('message'), 'status_code': response.get('status_code')}