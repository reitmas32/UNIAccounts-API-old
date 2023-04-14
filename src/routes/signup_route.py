
from services.db.idata_base import IDataBase
from models.user import User


def signup_route_POST(parameters_json: dict, data_base: IDataBase):
    new_user = User.from_dict(parameters_json)
    if new_user == None:
        return {'message': 'Error User no created', 'status_code': 428}
    message, status_code = data_base.create_user(new_user)
    response = {'message': message, 'status_code': status_code}
    return response