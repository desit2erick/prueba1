from sqlalchemy import Column, ForeignKey, SmallInteger, Boolean, TIMESTAMP, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import desc
from models import db


class UsuariosRoles(db.Model):
    __tablename__ = 'usuarios_roles'
    __table_args__ = {"schema":"seguridad"}

    codUsuarioRol = Column('cod_usuario_rol', SmallInteger, primary_key=True)
    usuarioCod = Column('usuario_cod', SmallInteger, ForeignKey('seguridad.usuarios.cod_usuario'))
    rolCod = Column('rol_cod', SmallInteger, ForeignKey('seguridad.roles.cod_rol'))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    rol = relationship('Roles', backref=backref('UsuariosRoles', lazy='select'))

    def listQuery(orderBy=None, codUsuarioRol=None, usuarioCod=None, rolCod=None, activo=None):
        # Construccion de query
        query = db.session.query(UsuariosRoles)

        # Filtros
        if codUsuarioRol:
            query = query.filter(UsuariosRoles.codUsuarioRol == codUsuarioRol)
        if usuarioCod:
            query = query.filter(UsuariosRoles.usuarioCod == usuarioCod)
        if rolCod:
            query = query.filter(UsuariosRoles.rolCod == rolCod)
        if activo != None:
            query = query.filter(UsuariosRoles.activo == activo)

        # Orden
        if orderBy:
            if orderBy == 'codUsuarioRol':
                query = query.order_by(UsuariosRoles.codUsuarioRol)
            elif orderBy == 'usuarioCod':
                query = query.order_by(UsuariosRoles.usuarioCod)
            elif orderBy == 'rolCod':
                query = query.order_by(UsuariosRoles.rolCod)
            elif orderBy == 'activo':
                query = query.order_by(desc(UsuariosRoles.activo))
            else:
                query = query.order_by(UsuariosRoles.codUsuarioRol)
        else:
            query = query.order_by(UsuariosRoles.codUsuarioRol)

        return query 