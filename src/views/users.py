# External Packages
from flask import Blueprint
import requests
from flask import request,render_template
import config as CONFIG
from routes.signup_route import *
from routes.signin_route import *
from routes.signout_route import *
from services.db.data_base_array import DataBase_Array


def check_service_permissions(service_name: str, end_point: str):
    """Verifies if the service is authorized to use the requested EndPoint

    Args:
        service_name (str)
        end_point (str)

    Returns:
        bool: [True] if valid permission, opposite case [False]
    """
    try:
        permissions = CONFIG.SERVICE_PERMISSIONS[service_name]
        for permission in permissions:
            if permission == end_point:
                return True
    except SystemError as e:
        print(e)

    return False

def valid_API_KEY(API_KEY: str):
    """Validates if an API_KEY is authorized for the use of the API

    Args:
        API_KEY (str)

    Returns:
        tuple[bool, str]: Status of API_KEY, name of the service to which the API_KEY belongs
    """
    for key in CONFIG.API_KEYS:
        value = CONFIG.API_KEYS[key]
        if value == API_KEY:
            return True, key
    return False, ''

def valid_credentials(_request, name_endpoint):
    status, service_name = CONFIG.valid_API_KEY(_request.headers.get('Api-Key'))
    response = ''
    
    if not status:
        return {'message': 'No API_KEY Valid',
                'status': False, 'service_name': '',
                'status_code': 403}
    
    if not CONFIG.check_service_permissions(service_name, name_endpoint):
        return {'message': 'API_KEY Valid but Permission Denied by this request',
                'status': False, 'service_name': '',
                'status_code': 403}

    return {'message': response, 'status': status, 'service_name': service_name, 'status_code': 200}


views_users = Blueprint('users', __name__)
data_base_service = DataBase_Array(views_users)


@views_users.route('/', methods=['GET'])
def index():
    """Respond with the API documentation

    Returns:
        str: API Documentation
    """
    api_docs = open(f"src/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()

@views_users.route('/test', methods=['GET'])
def test():
    """Test Route

    Returns:
        str:
    """
    return 'Hello World!!!'

@views_users.route('/api/v1/signup', methods=['POST', 'PUT'])
def signup():
    """SignUp EndPoint

    Returns:
        dict: JSON response
        int: status code of the request 
    """
    response_credentials = valid_credentials(request, f'signup_route_{request.method}')
    service_name = response_credentials.get('service_name')
    
    if response_credentials.get('status') == False:
        return response_credentials, response_credentials.get('status_code')
        
    if request.method == 'POST':
        response = signup_route_POST(request.json, data_base_service, service_name)
        status_code = response.get('status_code')
    
    return response, status_code

@views_users.route('/api/v1/signin', methods=['PUT', 'GET'])
def signin():
    """SignIn EndPoint

    Returns:
        dict: JSON response
        int: status code of the request 
    """
    response_credentials = valid_credentials(request, f'signin_route_{request.method}')
    service_name = response_credentials.get('service_name')
    
    if response_credentials.get('status') == False:
        return response_credentials, response_credentials.get('status_code')
    
    if not request.is_json and request.method != 'GET':
        return {'message': 'No content Type'}, 401
        
    if request.method == 'PUT':
        response = signin_route_PUT(request.json, data_base_service, service_name)
        status_code = response.get('status_code')
    
    if request.method == 'GET':
        response = signin_route_GET(request.headers['Authorization'].split(" ")[1], data_base_service, service_name)
        status_code = response.get('status_code')
    
    return response, status_code

@views_users.route('/api/v1/signout', methods=['PUT'])
def signout():
    """SignOut EndPoint

    Returns:
        dict: JSON response
        int: status code of the request 
    """
    response_credentials = valid_credentials(request, f'signout_route_{request.method}')
    service_name = response_credentials.get('service_name')
    
    if response_credentials.get('status') == False:
        return response_credentials, response_credentials.get('status_code')
        
    if request.method == 'PUT':
        response = signout_route_PUT(request.headers['Authorization'].split(" ")[1], data_base_service, service_name)
        status_code = response.get('status_code')
    
    return response, status_code

@views_users.route('/signup', methods=['GET', 'POST'])
def signup_users():
    """SignUp Form

    Returns:
        str: Form by SignUp
        -------------------
        dict: JSON response
    """
    if request.method == 'POST':
        # Obtener los datos del formulario de registro
        nick_name  = request.form['nick_name']
        password  = request.form['password']
        email  = request.form['email']
        name   = request.form['name']
        last_name_fathers   = request.form['last_name_fathers']
        last_name_mothers  = request.form['last_name_mothers']
        account_number  = request.form['account_number']
        careers  = request.form['careers']
        role   = request.form['role']
        role_key  = request.form['role_key']
        half_year = request.form['half_year']
        
        query = {
            'nick_name'         : nick_name,
            'password'          : password,
            'email'             : email,
            'name'              : name,
            'last_name_fathers' : last_name_fathers,
            'last_name_mothers' : last_name_mothers,
            'account_number'    : account_number,
            'careers'           : careers,
            'half_year'         : half_year,
            'role'              : role,
            'role_key'          : role_key,
        }
        
        response = requests.post('http://127.0.0.1:4000/api/v1/signup',json=query, headers={'API_KEY': CONFIG.API_KEYS.get('UNICA_MANAGER_ACCOUNTS_API')} )
        
        # Retornar la respuesta adecuada
        return response.text
    else:
        # Mostrar el formulario de registro
        return render_template('signup.html')
