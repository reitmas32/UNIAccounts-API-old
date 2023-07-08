from config.router import app
from flask_restx import Api, Resource, fields
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint, request

api = Api(app, version='1.0', title='API Flask', description='API Flask')

# Configura la interfaz de usuario de Swagger
SWAGGER_URL = '/docs/api/v1'
API_URL = '/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Flask"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)