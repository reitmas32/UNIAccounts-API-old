import os
import sys
from decouple import AutoConfig
BASE_DIR = os.path.dirname(
    (os.path.dirname(os.path.abspath(__file__)))
)

LIST_PATH_TO_ADD = [
    BASE_DIR
]
sys.path.extend(LIST_PATH_TO_ADD)

# IMPORT ENVIRONMENT VARIABLES
PATH_FILE_ENV = os.path.join(BASE_DIR, "config")
config = AutoConfig(search_path=PATH_FILE_ENV)


ENVIRONMENT = config("ENVIRONMENT")
SECRET_KEY_TOKEN = config("SECRET_KEY_TOKEN")
API_KEYS = dict( [ (key,value) for key,value in dict(config.config.repository.data).items() if key.startswith("API_KEY_UNICA") ] )
API_VERSION = 'v1'


SERVICE_PERMISSIONS = {
    'UNICA_STORE': [
        'signup_route_POST',
        'signin_route_PUT', 
        'signin_route_GET',
        'signout_route_PUT',
    ],
    'UNICA_MANAGER_ACCOUNTS_API': [
        'signup_route_POST', 
        'signin_route_PUT', 
        'signin_route_GET',
        'signout_route_PUT',
    ]
}

PORT = 4000

DEBUG = True

HOST = '0.0.0.0'


# SETTINGS ENV
if ENVIRONMENT == "local":
    from config.local import *
elif ENVIRONMENT == "develop":
    from config.development import *
elif ENVIRONMENT == "production":
    from config.production import *
else:
    raise ValueError("Debes especificar una variable de entorno ENVIRONMENT valida.")