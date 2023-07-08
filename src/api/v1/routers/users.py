# External Packages
from flask import Blueprint, request

from tools.functions_authentication import valid_headers

from ..views.users import signup_route_POST
from ..views.forgot_codes import forgot_password_POST, forgot_password_PUT

    
from flask_restx import Api, Resource, fields, Namespace
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint, request
from config.api_docs import api
from api.v1.schemas.users import *

signup_ns = Namespace('SignUp', description='Creacion de Cuentas', path='/api/v1/signup')
forgot_password_ns = Namespace('ForgotPassword', description='Restablecimiento de Contraseña', path='/api/v1/forgot-password')

@signup_ns.route('')
class SignUpResource(Resource):
    @api.doc(
    responses={
        201: 'Success signup, user create',
        401: 'Not API_KEY Valid',
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh', 'Service': 'uniaccounts'},
    description='Create a new user on the specified system and service'
    )
    @api.marshal_with(signup_response_201, code=201)
    @api.marshal_with(signup_response_401, code=401)
    @api.expect(user_schema_input, validate=False)
    def post(self):
        response_credentials, status_code = valid_headers(request)
        if not response_credentials.get("Success"):
            return response_credentials, status_code

        if request.method == "POST":
            response = signup_route_POST(parameters_json=request.get_json())
            return response
        

@forgot_password_ns.route('')
class ForgotPasswordResource(Resource):
    @api.doc(
    responses={
        201: 'Successful the code was sent by mail',
        400: 'Data invalid for create user',
        401: 'Not API_KEY Valid',
        500: 'Error for Forgot Password'
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh', 'Service': 'uniaccounts'},
    description="Request a password recovery code, the code will be sent by registered mail",
    )
    @api.marshal_with(forgot_password_post_response_201, code=201)
    @api.marshal_with(forgot_password_post_response_400, code=400)
    @api.marshal_with(forgot_password_post_response_401, code=401)
    @api.marshal_with(forgot_password_post_response_500, code=500)
    @api.expect(user_forgot_passord_schema_input, validate=False)
    def post(self):
        response_credentials, status_code = valid_headers(request)
        if not response_credentials.get("Success"):
            return response_credentials, status_code

        if request.method == "POST":
            response = forgot_password_POST(parameters_json=request.get_json())
            return response
        

    @api.doc(
    responses={
        201: 'Success forgot Password',
        400: 'Data invalid for create user',
        401: 'Not API_KEY Valid',
        403: 'Error No previous request for password change was found.',
        500: 'Error for Forgot Password'
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh', 'Service': 'uniaccounts'},
    description='Code validation for password recovery'
    )
    @api.marshal_with(forgot_password_put_response_201, code=201)
    @api.marshal_with(forgot_password_put_response_400, code=400)
    @api.marshal_with(forgot_password_put_response_401, code=401)
    @api.marshal_with(forgot_password_put_response_500, code=500)
    @api.expect(user_forgot_passord_confirm_schema_input, validate=False)
    def put(self):
        response_credentials, status_code = valid_headers(request)
        if not response_credentials.get("Success"):
            return response_credentials, status_code
        
        if request.method == "PUT":
            response = forgot_password_PUT(parameters_json=request.get_json())
            return response
    
# Agrega tus recursos a la API
api.add_namespace(signup_ns)
api.add_namespace(forgot_password_ns)
