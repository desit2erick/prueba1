from flask import Flask
from models import db
from resources import api, jwt, cors
from resources.jwt_errors import *
from settings import DevelopmentConfig

# Inicializando y configurando app
app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

# Inicializando extensiones
cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app)
jwt.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run()