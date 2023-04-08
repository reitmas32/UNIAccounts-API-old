from flask import Flask, request, jsonify

app = Flask(__name__)

# Create DataBase Conection
from services.db.data_base_mongodb import DataBase_MongoDB
data_base_service = DataBase_MongoDB(app)

import config as CONFIG
from routes.singup_route import *
from routes.singin_route import *

@app.route('/', methods=['GET'])
def index():
    api_docs = open(f"docs/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()

@app.route('/test', methods=['GET'])
def test():
    return 'Hello World!!!'

@app.route('/api/v1/singup', methods=['POST', 'PUT'])
def singup():
    status, service_name = CONFIG.valid_API_KEY(request.headers.get('API_KEY'))
    
    response = 'Nada'
    status_code = 404
    
    if not request.is_json:
        return 'No content Type'
    if not status:
        return 'No API_KEY Valid'
    
    if not CONFIG.check_service_permissions(service_name, f'singup_route_{request.method}'):
        return 'API_KEY Valid but Permission Denied by this request'
        
    if request.method == 'POST':
        response, status_code = singup_route_POST(request.json, data_base_service)
    
    return response, status_code

@app.route('/api/v1/singin', methods=['PUT', 'GET'])
def singin():
    status, service_name = CONFIG.valid_API_KEY(request.headers.get('API_KEY'))
    
    response = 'Nada'
    status_code = 404
    
    if not request.is_json and request.method != 'GET':
        return 'No content Type'
    if not status:
        return 'No API_KEY Valid', 401
    
    if not CONFIG.check_service_permissions(service_name, f'singin_route_{request.method}'):
        return 'API_KEY Valid but Permission Denied by this request', 403
        
    if request.method == 'PUT':
        response, status_code = singin_route_PUT(request.json, data_base_service)
    
    if request.method == 'GET':
        response = singin_route_GET(request.headers['Authorization'].split(" ")[1], data_base_service)
        status_code = response.get('status_code')
    
    return response, status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)