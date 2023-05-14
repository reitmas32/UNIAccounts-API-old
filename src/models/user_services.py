from config.database import db

from .base_model import BaseModelClass


class UserServicesModel(BaseModelClass):
    __tablename__ = "user_services"
    service_id = db.Column(db.String(36), db.ForeignKey("services.id"), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
