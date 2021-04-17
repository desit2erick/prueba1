from sqlalchemy import Column, ForeignKey, SmallInteger, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from models import db


class CategoriaPermisos(db.Model):
    __tablename__ = 'categoria_permisos'
    __table_args__ = {"schema":"seguridad"}

    codCategoriaPermiso = Column('cod_categoria_permiso', SmallInteger, primary_key=True)
    categoriaPermiso = Column('categoria_permiso', String(50))
    descripcion = Column('descripcion', String(200))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    permisos = relationship('Permisos', backref=backref('CategoriaPermisos', lazy='select'))