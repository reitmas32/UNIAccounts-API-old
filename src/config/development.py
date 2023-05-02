from .base import config

SQLALCHEMY_DATABASE_URI=config("SQLALCHEMY_DATABASE_URI")


# Create DataBase Conection
# 'mysql://<username>:<password>@<host>/<database_name>'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@<host>/<database_name>'
