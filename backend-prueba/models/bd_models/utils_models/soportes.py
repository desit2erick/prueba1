from sqlalchemy import Column, SmallInteger, String, Boolean, TIMESTAMP, ForeignKey
from models import db

class Soportes(db.Model):
    __tablename__ = 'soportes'
    __table_args__ = {"schema":"panales"}

    codSoporte = Column('cod_soporte', SmallInteger, primary_key=True)
    soporte = Column('soporte', String(25))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)
