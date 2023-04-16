######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 10/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# Local Packages
from models.user import User

class IDataBase:
    """Interface for connections to different databases
    """
    def __init__():
        pass
    
    def create_user(self, user: User, service_name: str):
        """Create a new User in DataBase

        Args:
            user (User): User to inserted
            service_name (str): Name of the service requested by the operation
        """
        pass
    
    def find_user(self, user: User, service_name: str):
        """Search a User in DataBase

        Args:
            user (User): User to search
            service_name (str): Name of the service requested by the operation
        """
        pass
    
    def signin_user(self, user: User, service_name: str):
        """Start a user's session

        Args:
            user (User): User to signin
            service_name (str): Name of the service requested by the operation
        """
        pass
    
    def signout_user(self, user: User, service_name: str):
        """End a user's session

        Args:
            user (User): User to signin
            service_name (str): Name of the service requested by the operation
        """
        pass
    
    def _create_new_session(self, JWT: str, service_name: str):
        """Create a new Session

        Args:
            JWT (str): JWT of user session
            service_name (str): Name of the service requested by the operation
        """
        pass
    
    def check_token_user(self, token_authorization: str, service_name: str):
        """verify that the session corresponding to the token is active 

        Args:
            token_authorization (str): JWT of session
            service_name (str): Name of the service requested by the operation

        Returns:
            dict: response of the operation in the DataBase
        """
        pass
    
