######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 19/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# System Packages
from werkzeug.security import check_password_hash

# Local Packages
from tools.funtions_jwt import write_token, validate_token
from models.user import User
from services.db.idata_base import IDataBase
import tools.functions_dict as TOOLS_Dict

def _check_password_match(user_request: dict, user: User):
    """Compare a hash password and a non-hash

    Args:
        user_request (dict): Data User
        user (User): User Object

    Returns:
        bool: [True] if passwords match
    """
    return check_password_hash(user_request.get("password"), user.password)


class DataBase_Array(IDataBase):
    """IDataBase implementation by Arrays
    """
    _data_base = None
    def __init__(self, app):
        """Constructor 

        Args:
            app (Flask): App Flask
        """
        # Local DB based to arrays
        self._data_base = {'sessions': [], 'users': []}
    
    def create_user(self, user: User, service_name: str):
        """Create a new User in DataBase

        Args:
            user (User): User to inserted
            service_name (str): Name of the service requested by the operation
        """
        # This is equal to findOne of PyMongo
        if next((item for item in self._data_base.get('users') if item["nick_name"] == user.nick_name ), None) != None:
            return 'Error nick_name in use', 428
        
        # This is equal to insertOne of PyMongo
        id = self._data_base.get('users').append(user.__dict__())
        print(self._data_base)
        return 'Succesfull signUp', 200
    
    def find_user(self, user: User, service_name: str):
        """Search a User in DataBase

        Args:
            user (User): User to search
            service_name (str): Name of the service requested by the operation
        """
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
        # This is equal to findOne of PyMongo
        request_data_base = next((item for item in self._data_base.get('users') if item[parameter_auth_key] == parameter_auth_value ), None)
        if request_data_base == None:
            return {'message':'Error no User Exist', 'status_code' :403}
        
        return {'message':'Succesfull signIn', 'status_code' :200, 'request_data_base': request_data_base}
    
    def signin_user(self, user: User, service_name: str):
        """Start a user's session

        Args:
            user (User): User to signin
            service_name (str): Name of the service requested by the operation
        """
        response_find_user = self.find_user(user, service_name)
        
        user_response = response_find_user.get("request_data_base")
        user_jwt = ''
        
        # Generate JWT
        if _check_password_match(user_response, user) == True:
            user.password = ''
            user_response['_id'] = ''
            user_response['password'] = ''
            user_jwt = write_token(data=user_response)
        else:
            return {'message':'Password Invalid', 'status_code' :403}
        
        
        response = {'message':'Succesfull signIn', 'status_code' :200, 'jwt': str(user_jwt, encoding='UTF-8'), 'service_name': service_name}
        
        if TOOLS_Dict.get_from_dict(response, 'status_code', default_value=0) != 200:
            return response
        _ = self._create_new_session(str(user_jwt, encoding='UTF-8'), service_name=service_name)
        return response
    
    def _create_new_session(self, JWT: str, service_name: str):
        """Create a new Session

        Args:
            JWT (str): JWT of user session
            service_name (str): Name of the service requested by the operation
        """
        # This is equal to insertOne of PyMongo
        return self._data_base.get('sessions').append({'JWT': JWT, 'service_name': service_name, 'status': 'ACTIVE'})
        
    def check_token_user(self, token_authorization: str, service_name: str):
        """verify that the session corresponding to the token is active 

        Args:
            token_authorization (str): JWT of session
            service_name (str): Name of the service requested by the operation

        Returns:
            dict: response of the operation in the DataBase
        """
        # Validate Token
        response_valid_token = validate_token(token=token_authorization)
        if response_valid_token.get('user') == '':
            
            # This is equal to replace_one of PyMongo
            try:
                _ = next((item for item in self._data_base.get('sessions') if item['JWT'] == token_authorization and item['service_name'] == service_name and item['status'] == 'ACTIVE' ), None)
                self._data_base.get('sessions').remove({'JWT': token_authorization,'service_name': service_name, 'status': 'ACTIVE'})
                self._data_base.get('sessions').append({'JWT': token_authorization,'service_name': service_name, 'status': 'DISABLED'})
            except:
                return {'message': 'SignOut Error The service is not the owner of the session', 'status_code': 401}
            return {'message': response_valid_token.get('message'), 'status_code': 401}
        
        # Find Active Session
        session_response = next((item for item in self._data_base.get('sessions') if item['JWT'] == token_authorization and item['service_name'] == service_name and item['status'] == 'ACTIVE' ), None)
        if session_response == None:
            return {'message': 'Sesion DISABLED', 'status_code': 401}
        
        # Return user data
        return response_valid_token
    
    def signout_user(self, token_authorization: str, service_name: str):
        """End a user's session

        Args:
            token_authorization (str): JWT of session
            service_name (str): Name of the service requested by the operation
        """
        # Validate Token
        response_valid_token = validate_token(token=token_authorization)
        if response_valid_token.get('user') == '':
            return {'message': response_valid_token.get('message'), 'status_code': 401}
        
        # This is equal to replace_one of PyMongo
        try:
            _ = next((item for item in self._data_base.get('sessions') if item['JWT'] == token_authorization and item['service_name'] == service_name and item['status'] == 'ACTIVE' ), None)
            self._data_base.get('sessions').remove({'JWT': token_authorization,'service_name': service_name, 'status': 'ACTIVE'})
            self._data_base.get('sessions').append({'JWT': token_authorization,'service_name': service_name, 'status': 'DISABLED'})
        except:
            return {'message': 'SignOut Error The service is not the owner of the session', 'status_code': 401}
        
        return {'message': 'SignOut Successful', 'status_code': 200}