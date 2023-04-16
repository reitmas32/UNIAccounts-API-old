######################################################################
# author = Rafael Zamora
# copyright = Copyright 2023, UNICA-ManagerAccounts
# date = 16/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# Local Packages
from services.db.idata_base import IDataBase

def signout_route_PUT(token_authorization: str, data_base: IDataBase, service_name: str):
    """EndPoint /signout with method HTTP PUT, SignOut Session 

    Args:
        token_authorization (str): JWT of session
        data_base (IDataBase): Implementation of the database to be used
        service_name (str): Name of the service requested by the operation

    Returns:
        dict: response of the operation in the DataBase
    """
    response = data_base.signout_user(token_authorization, service_name)
    return response