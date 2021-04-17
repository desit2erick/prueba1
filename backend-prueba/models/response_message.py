from flask_restx import fields, marshal

mensajeFields = {'message': fields.String}

def messageHandler(msg, codigo=510):
    return marshal({'message': msg}, mensajeFields), codigo