# External Packages
from flask import Flask
from flask_migrate import Migrate

import config.base as CONFIG
from api.v1.routers.core import views_core
from api.v1.routers.user_services import views_user_services

# Local Packages
from config.database import db

from config.router import app
from config.api_docs import api
import api.v1.routers.users
import api.v1.routers.service
import api.v1.routers.validate_token
import api.v1.routers.development.services
import api.v1.routers.development.users
app.register_blueprint(views_user_services)
app.register_blueprint(views_core)


app.config["SQLALCHEMY_DATABASE_URI"] = CONFIG.SQLALCHEMY_DATABASE_URI
app.config["DATABASE_PATH"] = CONFIG.BASE_DIR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
