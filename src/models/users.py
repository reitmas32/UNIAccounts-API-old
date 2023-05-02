from config.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    careers = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    exp = db.Column(db.Integer, nullable=False)
    half_year = db.Column(db.Integer, nullable=False)
    last_name_fathers = db.Column(db.String(80), nullable=False)
    last_name_mothers = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    nick_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    role_key = db.Column(db.String(80), nullable=False)
