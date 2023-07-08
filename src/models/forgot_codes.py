from config.database import db

from .base_model import BaseModelClass


class ForgotCodeModel(BaseModelClass):
    __tablename__ = "forgot_codes"
    user_name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)

    def toJSON(self):
        return {
            "code": self.code,
            "user_name": self.user_name,
            "updated": self.updated.strftime('%Y-%m-%d %H:%M:%S'),
            "created": self.created.strftime('%Y-%m-%d %H:%M:%S'),
            "is_removed": self.is_removed,
        }