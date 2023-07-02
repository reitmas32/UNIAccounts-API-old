from datetime import datetime

from pydantic import BaseModel, EmailStr, validator, ValidationError


class ServiceSchema(BaseModel):
    name: str
    mother_login: bool
    jwt_exp: int