from tools.funtions_jwt import write_token, validate_token
from models.user import User
from services.db.idata_base import IDataBase
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash


class DataBase_MongoDB(IDataBase):
    _data_base = None
    def __init__(self, app):
        app.config["MONGO_URI"] = "mongodb://localhost/test_db"
        self._data_base = PyMongo(app)
    
    def create_user(self, user: User):
        if self._data_base.db.users.find_one({'nick_name': user.nick_name}) != None:
            return 'Error nick_name in use', 428
        print(user.password)
        id = self._data_base.db.users.insert_one(user.__dict__())
        return 'Succesfull SingUp', 200
    
    def find_user(self, user: User):
        parameter_auth_key = ''
        parameter_auth_value = ''
        if user.account_number != None:
            parameter_auth_key = 'account_number'
            parameter_auth_value = user.account_number
        elif user.nick_name != None:
            parameter_auth_key = 'nick_name'
            parameter_auth_value = user.nick_name
        elif user.email != None:
            parameter_auth_key = 'email'
            parameter_auth_value = user.email
            
        request_mongodb = self._data_base.db.users.find_one({parameter_auth_key: parameter_auth_value})
        if request_mongodb == None:
            return {'message':'Error no User Exist', 'status_code' :403}
        
        if check_password_hash(request_mongodb.get("password"), user.password) == True:
            user.password = ''
            user_jwt = write_token(data=user.__dict__())
        else:
            return {'message':'Password Invalid', 'status_code' :403}
        return {'message':'Succesfull SingIn', 'status_code' :200, 'jwt': str(user_jwt, encoding='UTF-8')}
    
    def check_token_user(self, token_authorization):
        response_valid_token = validate_token(token=token_authorization)
        response = {}
        if response_valid_token.get('status'):
            response = {'message': response_valid_token.get('message'), 'status_code': 200}
        else:
            response = {'message': response_valid_token.get('message'), 'status_code': 401}
            
        return response
        