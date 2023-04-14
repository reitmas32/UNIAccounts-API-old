from models.user import User


class IDataBase:
    def __init__():
        pass
    
    def create_user(self, user: User, service_name: str):
        pass
    
    def find_user(self, user: User, service_name: str):
        pass
    
    def signin_user(self, user: User, service_name: str):
        pass
    
    def _create_new_session(self, JWT: str, service_name: str):
        pass
    
