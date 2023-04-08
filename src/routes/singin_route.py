from services.db.idata_base import IDataBase
from models.user import User


def singin_route_PUT(parameters_json: dict, data_base: IDataBase):
    new_user, message, status_code = User.from_dict_password_nohash(parameters_json)
    if new_user == None:
        return {'message': f'Error {message}', 'status_code': status_code}, status_code
    message, status_code = data_base.find_user(new_user)
    request = {'message': message, 'status_code': status_code}
    return request, status_code