from datetime import datetime

from pydantic import BaseModel, EmailStr, validator, ValidationError
from flask_restx import fields
from config.api_docs import api


class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    user_name: str
    phone_number: str
    date_of_birth: datetime
    password: str
    role: str
    
    @validator('date_of_birth', pre=True)
    def validate_date_of_birth(cls, value):
        return datetime.strptime(value, "%d-%m-%Y")
            
# Define el modelo de entrada utilizando fields del objeto api
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

signup_response_201 = api.model('Response', {
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

signup_response_401 = api.model('Response', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example='Not API_KEY Valid')
}
)


class UserSigninSchema(BaseModel):
    user_name: str
    password: str

user_forgot_passord_confirm_schema_input = api.model('ForgotCodesPasswordSchema', {
    'user_name': fields.String(required=True, example='rafa_user_zam'),
    'password': fields.String(required=True, example='new_password'),
    'code': fields.String(required=True, example='784598'),

})

forgot_password_put_response_201 = api.model('Response', {
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

forgot_password_put_response_400 = api.model('Response', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Data invalid for reset password"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)

forgot_password_put_response_401 = api.model('Response', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Not API_KEY Valid'))
}
)

forgot_password_put_response_403 = api.model('Response', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Error No previous request for password change was found.'))
}
)

forgot_password_put_response_500 = api.model('Response', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Error for Forgot Password"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)
    
class UserForgotPasswordSchema(BaseModel):
    user_name: str

user_forgot_passord_schema_input = api.model('UserForgotPasswordSchema', {
    'user_name': fields.String(required=True, example='rafa_user_zam'),
})

forgot_password_post_response_201 = api.model('Response', {
    "Success": fields.Boolean(required=True, example=True),
        "Message": fields.String(required=True, example='Successful the code was sent by mail'),
        "Data": fields.Raw(required=True, example={
            "user_name": 'rafa_user_zam',
            "user_email": 'rafa@gmail.com',
        })
})

forgot_password_post_response_400 = api.model('Response', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Data invalid for create user"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)

forgot_password_post_response_401 = api.model('Response', {
  "Data": fields.Raw(required=True, example={}),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example=fields.String(required=True, example='Not API_KEY Valid'))
}
)

forgot_password_post_response_500 = api.model('Response', {
        "Success": fields.Boolean(required=True, example=False),
        "Message": fields.String(required=True, example="Error for create ForgotCode"),
        "Data": fields.Raw(required=True, example={"errors": '...'}),
    }
)