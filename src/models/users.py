from config.database import db

from .base_model import BaseModelClass


class UsersModel(BaseModelClass):
    __tablename__ = "users"
    name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def toJSON(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "user_name": self.user_name,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth.strftime('%Y-%m-%d %H:%M:%S'),
            "role": self.role,
            "updated": self.updated.strftime('%Y-%m-%d %H:%M:%S'),
            "created": self.created.strftime('%Y-%m-%d %H:%M:%S'),
            "is_removed": self.is_removed,
        }

