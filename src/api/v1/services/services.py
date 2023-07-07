from typing import Dict

import config.base as CONFIG
from config.database import get_session
from models import ServicesModel

from ..schemas import ServiceSchema

from tools.random_string import generate_random_string


class ServicesService:
    def get_services(self) -> Dict[str, "ServicesModel"]:
        if not CONFIG.API_KEYS:
            session = get_session()
            services = session.query(ServicesModel).all()
            session.close()
            CONFIG.API_KEYS = {service.name: service for service in services}
        return CONFIG.API_KEYS
    
    def create_service(self, service_data: ServiceSchema) -> ServicesModel:
        session = get_session()
        service = ServicesModel(
            name=service_data.name, 
            api_key=generate_random_string(32), 
            jwt_exp=service_data.jwt_exp, 
            mother_login=service_data.mother_login,
        )
        session.add(service)
        session.commit()
        #session.close()
        return service
