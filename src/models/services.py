from config.database import db

from .base_model import BaseModelClass


class ServicesModel(BaseModelClass):
    __tablename__ = "services"
    name = db.Column(db.String(255), nullable=False)
    mother_login = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String(255), nullable=False)
    jwt_exp = db.Column(db.Integer, nullable=False)

    def toJSON(self):
        return {
            "name": self.name,
            "mother_login": self.mother_login,
            "api_key": self.api_key,
            "jwt_exp": self.jwt_exp,
            "id": self.id,
            "updated": self.updated.strftime('%Y-%m-%d %H:%M:%S'),
            "created": self.created.strftime('%Y-%m-%d %H:%M:%S'),
            "is_removed": self.is_removed,
        }
