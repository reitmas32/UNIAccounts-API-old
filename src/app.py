# External Packages
from flask import Flask
from flask_migrate import Migrate

# Local Packages
from views.users import views_users
import config as CONFIG
from config.database import db

app = Flask(__name__)
app.register_blueprint(views_users)

app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Inicialización de Flask-Migrate en todas las rutas de su proyecto en busca de modelos
# migrate.init_app(app, db, directory='models')

# flask db init: 
# este comando inicializa el directorio de migraciones en el proyecto, 
# creando una carpeta llamada migrations en la raíz del proyecto.

# flask db migrate: 
# este comando detecta los cambios en los modelos y genera un archivo 
# de migración en la carpeta migrations.

# flask db upgrade: 
# este comando aplica las migraciones pendientes al esquema de la base 
# de datos, creando o actualizando las tablas según sea necesario.

