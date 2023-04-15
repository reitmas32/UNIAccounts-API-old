######################################################################
# author = Rafael Zamora
# copyright = Copyright 2020-2023, UNICA-ManagerAccounts
# date = 06/04/2023
# license = PSF
# version = 1.0
# maintainer = Rafael Zamora
# email = rafa.zamora.rals@gmail.com
# status = Development
######################################################################

# Local Packages
import ENVS

API_VERSION = 'v1'

SERVICE_PERMISSIONS = {
    'UNICA_STORE': ['signup_route_POST', 'signin_route_PUT', 'signin_route_GET'],
    'UNICA_MANAGER_ACCOUNTS_API': ['signup_route_POST', 'signin_route_PUT', 'signin_route_GET']
}

PORT = 4000

DEBUG = True

HOST = '0.0.0.0'


def valid_API_KEY(API_KEY: str):
    """Validates if an API_KEY is authorized for the use of the API

    Args:
        API_KEY (str)

    Returns:
        tuple[bool, str]: Status of API_KEY, name of the service to which the API_KEY belongs
    """
    for key in ENVS.API_KEYS:
        value = ENVS.API_KEYS[key]
        if value == API_KEY:
            return True, key
    return False, ''


def check_service_permissions(service_name: str, end_point: str):
    """Verifies if the service is authorized to use the requested EndPoint

    Args:
        service_name (str)
        end_point (str)

    Returns:
        bool: [True] if valid permission, opposite case [False]
    """
    try:
        permissions = SERVICE_PERMISSIONS[service_name]
        for permission in permissions:
            if permission == end_point:
                return True
    except SystemError as e:
        print(e)

    return False
