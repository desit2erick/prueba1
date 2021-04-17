from models import messageHandler
from resources import jwt
 
@jwt.expired_token_loader
def expired_toke(callback):
    return messageHandler('La sesión expiró', 401)

@jwt.invalid_token_loader
def expired_token(callback):
    return messageHandler('Token inválido', 422)

@jwt.unauthorized_loader
def unauthorized(callback):
    return messageHandler('No se ha iniciado sesión', 401)