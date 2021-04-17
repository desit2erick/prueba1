from sqlalchemy import Column, SmallInteger, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import desc
from models import db


class Roles(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {"schema":"seguridad"}

    codRol = Column('cod_rol', SmallInteger, primary_key=True)
    rol = Column('rol', String(50))
    descripcion = Column('descripcion', String(200))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    rolesPermisos = relationship('RolesPermisos', backref=backref('Roles', lazy='select'))
    rolesUsuarios = relationship('UsuariosRoles', backref=backref('Roles', lazy='select'))


    def listQuery(orderBy=None, codRol=None, nombre=None, activo=None):
        # Construccion de query
        query = db.session.query(Roles)
        
        # Filtros
        if codRol:
            query = query.filter(Roles.codRol == codRol)
        if nombre:
            query = query.filter(Roles.rol.ilike('%'+nombre+'%'))
        if activo != None:
            query = query.filter(Roles.activo == activo)

        # Orden
        if orderBy:
            if orderBy == 'rol':
                query = query.order_by(Roles.rol)
            elif orderBy == 'activo':
                query = query.order_by(desc(Roles.activo))
            else:
                query = query.order_by(Roles.rol)
        else:
            query = query.order_by(Roles.rol)

        return query