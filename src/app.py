from flask import Flask, request, jsonify

app = Flask(__name__)

import config as CONFIG
from routes.singup_route import *

@app.route('/', methods=['GET'])
def index():
    api_docs = open(f"docs/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()

@app.route('/api/v1/singup', methods=['POST', 'PUT'])
def singup():
    status, service_name = CONFIG.valid_API_KEY(request.headers.get('API_KEY'))
    
    response = 'Nada'
    
    if not request.is_json:
        return 'No content Type'
    if not status:
        return 'No API_KEY Valid'
    
    if not CONFIG.check_service_permissions(service_name, f'singup_route_{request.method}'):
        return 'API_KEY Valid but Permission Denied by this request'
        
    if request.method == 'POST':
        response = singup_route_POST(request.json)
    
    return response