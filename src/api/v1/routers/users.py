# External Packages
from flask import Blueprint, request

from tools.functions_authentication import valid_headers

from ..views.users import signup_route_POST
from ..views.forgot_codes import forgot_password_POST, forgot_password_PUT
from ..views.core import signin_route_PUT

    
from flask_restx import Api, Resource, fields, Namespace
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint, request
from config.api_docs import api

signup_ns = Namespace('SignUp', description='SignUp Users', path='/api/v1')
signin_ns = Namespace('SignIn', description='Login Users', path='/api/v1')
forgot_password_ns = Namespace('ForgotPassword', description='Restablecimiento de Contraseña', path='/api/v1')

user_schema_input = api.model('UserSchema', {
    'name': fields.String(required=True, example='Rafael'),
    'last_name': fields.String(required=True, example='Zamora'),
    'email': fields.String(required=True, example='rafa@gmail.com'),
    'user_name': fields.String(required=True, example='rafa_user_zam'),
    'phone_number': fields.String(required=True, example='5546897812'),
    'date_of_birth': fields.DateTime(required=True, example='11-01-2000'),
    'password': fields.String(required=True, example='this_no_security_pasword'),
    'role': fields.String(required=True, example='admin'),
})

signup_response_201 = api.model('signup.respoonse.201', {
    'Data': fields.Raw(required=True, example={
    'name': 'rafa',
    'last_name': 'zamora',
    'email': 'rafa@gmail.com',
    'user_name': 'rafa_user_zam',
    'phone_number': '5546897812',
    'date_of_birth': '11-01-2000',
    'password': '',
    'role': 'admin',
}),
    'Successful': fields.Boolean(required=True, example=True),
    'Message': fields.String(required=True, example='Successful Response'),
})

signup_response_401 = api.model('signup.response.401', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example='Not API_KEY Valid')
}
)

@signup_ns.route('/signup')
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
        
@signin_ns.route('/signin')
class SignInResource(Resource):
    @api.doc(
    responses={
        201: 'Success signin, user create',
        401: 'Not API_KEY Valid',
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh', 'Service': 'uniaccounts'},
    description='Login User in Service'
    )
    @api.marshal_with(signup_response_201, code=201)
    @api.marshal_with(signup_response_401, code=401)
    @api.expect(user_schema_input, validate=False)
    def put(self):
        response_credentials, status_code = valid_headers(request)
        if not response_credentials.get("Success"):
            return response_credentials, status_code

        if request.method == "PUT":
            response = signin_route_PUT(request=request)
            return response
        
#PUT

user_forgot_passord_confirm_schema_input = api.model('ForgotCodesPasswordSchema', {
    'user_name': fields.String(required=True, example='rafa_user_zam'),
    'password': fields.String(required=True, example='new_password'),
    'code': fields.String(required=True, example='784598'),

})

forgot_password_put_response_201 = api.model('forgot_password.response.201', {
    'Data': fields.Raw(required=True, example={
    'name': 'rafa',
    'last_name': 'zamora',
    'email': 'rafa@gmail.com',
    'user_name': 'rafa_user_zam',
    'phone_number': '5546897812',
    'date_of_birth': '11-01-2000',
    'role': 'admin',
}),
    'Successful': fields.Boolean(required=True, example=True),
    'Message': fields.String(required=True, example='Success forgot Password'),
})

forgot_password_put_response_400 = api.model('forgot_password.put.response.400', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Data invalid for reset password"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)

forgot_password_put_response_401 = api.model('forgot_password.put.response.401', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Not API_KEY Valid'))
}
)

forgot_password_put_response_403 = api.model('forgot_password.put.response.403', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Error No previous request for password change was found.'))
}
)

forgot_password_put_response_500 = api.model('forgot_password.put.response.500', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Error for Forgot Password"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)

#POST

user_forgot_passord_schema_input = api.model('UserForgotPasswordSchema', {
    'user_name': fields.String(required=True, example='rafa_user_zam'),
})

forgot_password_post_response_201 = api.model('forgot_password.post.response.201', {
    "Success": fields.Boolean(required=True, example=True),
        "Message": fields.String(required=True, example='Successful the code was sent by mail'),
        "Data": fields.Raw(required=True, example={
            "user_name": 'rafa_user_zam',
            "user_email": 'rafa@gmail.com',
        })
})

forgot_password_post_response_400 = api.model('forgot_password.post.response.400', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Data invalid for create user"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)

forgot_password_post_response_401 = api.model('forgot_password.post.response.401', {
  #"Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Not API_KEY Valid'))
}
)

forgot_password_post_response_500 = api.model('forgot_password.post.response.500', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Error for create ForgotCode"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
) 

@forgot_password_ns.route('/forgot-password')
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
    #@api.marshal_with(forgot_password_post_response_401, code=401)
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
    #@api.marshal_with(forgot_password_put_response_401, code=401)
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
api.add_namespace(signin_ns)
api.add_namespace(forgot_password_ns)
