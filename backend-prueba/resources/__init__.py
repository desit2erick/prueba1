from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api

cors = CORS()
jwt = JWTManager()
api = Api(
    title='Woodstock UX API',
    version='1.2',
    description='API utilizada para el desarrollo y gestión de las operaciones relacionadas a Grupo Real Caruz',
)
api.prefix='/api'

from .namespaces import listaNamespaces

for ns in listaNamespaces:
    api.add_namespace(ns[0], path=ns[1])