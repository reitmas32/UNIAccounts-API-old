import uuid

from sqlalchemy_utils import Timestamp, UUIDType

from config.database import db


class BaseModelClass(Timestamp, db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_removed = db.Column(db.Boolean, nullable=False, default=False)
