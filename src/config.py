API_VERSION = 'v1'

SERVICE_PERMISSIONS = {
    'UNICA_STORE': ['signup_route_POST', 'signin_route_PUT', 'signin_route_GET'],
    'UNICA_MANAGER_ACCOUNTS_API': ['signup_route_POST', 'signin_route_PUT', 'signin_route_GET']
}

PORT = 4000

DEBUG = True

HOST = '0.0.0.0'

import ENVS

def valid_API_KEY(API_KEY: str) :
    for key in ENVS.API_KEYS:
        value = ENVS.API_KEYS[key]
        if value == API_KEY:
            return True, key
    return False, ''

def check_service_permissions(service_name: str, permission_route: str):
    try:
        permissions = SERVICE_PERMISSIONS[service_name]
        for permission in permissions:
            if permission == permission_route:
                return True
    except SystemError as e:
        print(e)
        
    return False