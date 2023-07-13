# External Packages
from flask import Blueprint, request
from flask import render_template
import json
import requests
import config.base as CONFIG

from tools.functions_authentication import valid_headers

from ..views.service import register_service_route_POST
from config.api_docs import api
from flask_restx import Api, Resource, fields, Namespace

service_ns = Namespace('Service', description='Services', path='/api/v1')

register_service_response_201 = api.model('register_service.response.201', {
    'Data': fields.Raw(required=True, example='[...]'),
    'Success': fields.Boolean(required=True, example=True),
    'Message': fields.String(required=True, example='Success Response'),
})

register_service_response_401 = api.model('register_service.response.401', {
  "Data": fields.Raw(required=True, example=[]),
  "Success": fields.Boolean(required=True, example=True),
  "Message": fields.String(required=True, example='Not API_KEY Valid')
}
)

register_service_request = api.model('ServiceSchema', {
    'name': fields.String(required=True, example='uniaccounts'),
    'mother_login': fields.Boolean(required=True, example=True, description='True if you sistem no register personal passwords'),
    'jwt_exp': fields.Integer(required=True, example=5, description='minutes expired this JWT'),
})

@service_ns.route('/register_service')
class ServicesResource(Resource):
    @api.doc(
    responses={
        201: 'Success signup, user create',
        401: 'Not API_KEY Valid',
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh'},
    description='Create a new user on the specified system and service'
    )
    @api.marshal_with(register_service_response_201, code=201)
    @api.marshal_with(register_service_response_401, code=401)
    @api.expect(register_service_request, validate=False)
    def post(self):

        api_key=request.headers.get("Api-Key")

        if api_key != CONFIG.API_KEY:
            response = {
                "Success": False,
                "Message": "Not API_KEY Valid",
                "Data": {},
            }

            return response

        if request.method == "POST":
            response = register_service_route_POST(parameters_json=request.get_json())
            return response

api.add_namespace(service_ns)