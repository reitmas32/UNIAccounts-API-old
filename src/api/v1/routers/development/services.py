# External Packages
from flask import request
from http import HTTPStatus
from config.api_docs import api
from flask_restx import Resource, fields, Namespace


import config.base as CONFIG

development = Namespace('Development', description='Services', path='/api/v1/development')

development_services_response_200 = api.model('development.services.get.response.200', {
    'Data': fields.Raw(required=True, example='[...]'),
    'Successful': fields.Boolean(required=True, example=True),
    'Message': fields.String(required=True, example='Success Get Services'),
})

register_service_response_400 = api.model('development.services.get.response.400', {
  "Data": fields.Raw(required=True, example=[]),
  "Successful": fields.Boolean(required=True, example=False),
  "Message": fields.String(required=True, example='Not API_KEY Valid')
}
)

@development.route('/services')
class ServicesResource(Resource):
    @api.doc(
    responses={
        201: 'Success Get Services',
        401: 'Not API_KEY Valid',
        },
    headers={'Api-Key': 'sEw7CMS03iJRI3EzVm1sYHfeqwQT6uZh'},
    description='Get all services'
    )
    @api.marshal_with(development_services_response_200, code=200)
    @api.marshal_with(register_service_response_400, code=400)
    def get(self):

        api_key=request.headers.get("Api-Key")

        if api_key != CONFIG.API_KEY:
            response = {
                "Success": False,
                "Message": "Not API_KEY Valid",
                "Data": {},
            }

            return response,  HTTPStatus.BAD_REQUEST

        from config.database import get_session
        from models import ServicesModel
        import json
        from datetime import datetime
        session = get_session()
        services = (
            session.query(ServicesModel).all()
        )
        session.close()

        # Convertir la lista de objetos SQLAlchemy a una lista de diccionarios JSON
        services_json = []

        for service in services:
            services_json.append(service.toJSON())
        
        response = {
            "Success": True,
            "Message": "Success Get Services",
            "Data":   services_json,
        }
        return response, HTTPStatus.CREATED

api.add_namespace(development)