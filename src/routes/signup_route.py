
from services.db.idata_base import IDataBase
from models.user import User


def signup_route_POST(parameters_json: dict, data_base: IDataBase):
    new_user, message, status_code = User.from_dict(parameters_json)
    if new_user == None:
        return {'message': f'Error {message}', 'status_code': status_code}
    message, status_code = data_base.create_user(new_user)
    response = {'message': message, 'status_code': status_code}
    return response