import requests

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Create DataBase Conection
from services.db.data_base_mongodb import DataBase_MongoDB
data_base_service = DataBase_MongoDB(app)

import config as CONFIG
import ENVS
from routes.signup_route import *
from routes.signin_route import *

@app.route('/', methods=['GET'])
def index():
    api_docs = open(f"api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()

@app.route('/test', methods=['GET'])
def test():
    return 'Hello World!!!'

@app.route('/api/v1/signup', methods=['POST', 'PUT'])
def signup():
    status, service_name = CONFIG.valid_API_KEY(request.headers.get('API_KEY'))
    
    response = 'Nada'
    status_code = 404
    
    if not request.is_json:
        return 'No content Type'
    if not status:
        return 'No API_KEY Valid'
    
    if not CONFIG.check_service_permissions(service_name, f'signup_route_{request.method}'):
        return 'API_KEY Valid but Permission Denied by this request'
        
    if request.method == 'POST':
        response = signup_route_POST(request.json, data_base_service, service_name)
        status_code = response.get('status_code')
    
    return response, status_code

@app.route('/api/v1/signin', methods=['PUT', 'GET'])
def signin():
    status, service_name = CONFIG.valid_API_KEY(request.headers.get('API_KEY'))
    
    response = 'Nada'
    status_code = 404
    
    if not request.is_json and request.method != 'GET':
        return 'No content Type'
    if not status:
        return 'No API_KEY Valid', 401
    
    if not CONFIG.check_service_permissions(service_name, f'signin_route_{request.method}'):
        return 'API_KEY Valid but Permission Denied by this request', 403
        
    if request.method == 'PUT':
        response = signin_route_PUT(request.json, data_base_service, service_name)
        status_code = response.get('status_code')
    
    if request.method == 'GET':
        response = signin_route_GET(request.headers['Authorization'].split(" ")[1], data_base_service)
        status_code = response.get('status_code')
    
    return response, status_code

@app.route('/signup', methods=['GET', 'POST'])
def signup_users():
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
        
        response = requests.post('http://127.0.0.1:4000/api/v1/signup',json=query, headers={'API_KEY': ENVS.API_KEYS.get('UNICA_MANAGER_ACCOUNTS_API')} )
        
        # Retornar la respuesta adecuada
        return response.text
    else:
        # Mostrar el formulario de registro
        return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)