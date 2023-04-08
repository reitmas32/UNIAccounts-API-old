import json
from models.user import User
from services.db.idata_base import IDataBase
from flask_pymongo import PyMongo


class DataBase_MongoDB(IDataBase):
    _data_base = None
    def __init__(self, app):
        app.config["MONGO_URI"] = "mongodb://localhost/test_db"
        self._data_base = PyMongo(app)
    
    def create_user(self, user: User):
        if self._data_base.db.users.find_one({'nick_name': user.nick_name}) != None:
            return 'Error nick_name in use', 428
        id = self._data_base.db.users.insert_one(user.__dict__())
        return 'Succesfull SingUp', 200
        