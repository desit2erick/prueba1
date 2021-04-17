from sqlalchemy import Column, BigInteger, SmallInteger, String, TIMESTAMP
from models import db

class Bitacoras(db.Model):
    __tablename__ = 'bitacoras'

    codBitacora = Column('cod_bitacora', BigInteger, primary_key=True)
    codRegistro = Column('cod_registro', BigInteger)
    tabla = Column('tabla', String(20))
    usuarioCod = Column('usuario_cod', SmallInteger)
    accion = Column('accion', String(50))
    fecha = Column('fecha', TIMESTAMP)
    descripcion = Column('descripcion', String(100))