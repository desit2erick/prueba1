from flask_jwt_extended import get_jwt_identity
from sqlalchemy import inspect
from datetime import datetime
from models import db, Bitacoras


def cargarBitacora(objeto, accion, descripcion=None):
    bitacora = Bitacoras(
        codRegistro = inspect(objeto).identity[0],
        tabla = objeto.__tablename__,
        usuarioCod = get_jwt_identity() if get_jwt_identity()!=None else inspect(objeto).identity[0],
        accion = accion, 
        fecha = datetime.now(),
        descripcion=descripcion
    )
    db.session.add(bitacora)
    db.session.commit()