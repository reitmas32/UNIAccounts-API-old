from config.api_docs import api
from flask_restx import Api, Resource, fields, Namespace
from flask import request

from ..views.core import validate_token_route_GET
from tools.functions_authentication import valid_headers

validate_token_ns = Namespace('Validate Token', description='Validate JWT of Users', path='/api/v1')

validate_token_response_200 = api.model('validate_token.response.200', {
    'Data': fields.String(required=True, example=''),
    'Successful': fields.Boolean(required=True, example=True),
    'Message': fields.String(required=True, example='Success token'),
})

validate_token_response_401 = api.model('validate_token.response.401', {
  "Data": fields.Raw(required=True, example=[]),
  "Successful": fields.Boolean(required=True, example=True),
  "Message": fields.String(required=True, example='Not API_KEY Valid')
}
)

@validate_token_ns.route('/validate_token')
class ServicesResource(Resource):
    @api.doc(
    responses={
        200: 'Success signup, user create',
        401: 'Not API_KEY Valid',
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh', 'Service': 'uniaccounts', 'JWT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'},
    description='Create a new user on the specified system and service'
    )
    @api.marshal_with(validate_token_response_200, code=200)
    @api.marshal_with(validate_token_response_401, code=401)
    def get(self):

        response_credentials, status_code = valid_headers(request)
        if not response_credentials.get("Success"):
            return response_credentials, status_code

        if request.method == "GET":
            response = validate_token_route_GET(request=request)
            return response

api.add_namespace(validate_token_ns)