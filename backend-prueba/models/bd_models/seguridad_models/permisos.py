from sqlalchemy import Column, ForeignKey, SmallInteger, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from models import db


class Permisos(db.Model):
    __tablename__ = 'permisos'
    __table_args__ = {"schema":"seguridad"}

    codPermiso = Column('cod_permiso', SmallInteger, primary_key=True)
    permiso = Column('permiso', String(50))
    descripcion = Column('descripcion', String(200))
    categoriaPermisoCod = Column('categoria_permiso_cod', SmallInteger, ForeignKey('seguridad.categoria_permisos.cod_categoria_permiso'))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    rolPermiso = relationship('RolesPermisos', backref=backref('Permisos', lazy='select'))