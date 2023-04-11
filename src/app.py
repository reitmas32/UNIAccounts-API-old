from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Create DataBase Conection
from services.db.data_base_mongodb import DataBase_MongoDB
data_base_service = DataBase_MongoDB(app)

import config as CONFIG
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
        response = signup_route_POST(request.json, data_base_service)
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
        response = signin_route_PUT(request.json, data_base_service)
        status_code = response.get('status_code')
    
    if request.method == 'GET':
        response = signin_route_GET(request.headers['Authorization'].split(" ")[1], data_base_service)
        status_code = response.get('status_code')
    
    return response, status_code


@app.route('/signup', methods=['GET', 'POST'])
def signup_users():
    if request.method == 'POST':
        # Obtener los datos del formulario de registro
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        print('Nuevo Usuario')

        # Validar los datos del formulario de registro
        # (Aquí puedes agregar tu lógica de validación, por ejemplo, consultar una base de datos para verificar si el usuario ya existe)

        # Si los datos son válidos, se realiza el registro
        # (Aquí puedes agregar tu lógica de registro, por ejemplo, agregar el usuario a una base de datos)

        # Retornar la respuesta adecuada
        return jsonify({'message': 'Registro exitoso. ¡Bienvenido a nuestra aplicación!'})
    else:
        # Mostrar el formulario de registro
        return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)