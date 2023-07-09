from config.router import app
from flask_restx import Api, Resource, fields
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint, request

api = Api(app, version='1.0', title='UNIAccount API', description='API to Manage UNICA System Accounts', license='Apache 2.0')

# Configura la interfaz de usuario de Swagger
SWAGGER_URL = '/docs/api/v1'
API_URL = '/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "UNIAccount API"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)