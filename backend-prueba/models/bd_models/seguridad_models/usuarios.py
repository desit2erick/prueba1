from sqlalchemy import Column, SmallInteger, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import desc
from models import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {"schema":"seguridad"}

    codUsuario = Column('cod_usuario', SmallInteger, primary_key=True)
    nombre = Column('nombre', String(50))
    apellido = Column('apellido', String(50))
    correo = Column('correo', String(50))
    usuario = Column('usuario', String(50))
    password = Column('password', String(60))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    rolesUsuario = relationship('UsuariosRoles', backref=backref('Usuario', lazy='select'))

    def listQuery(orderBy=None, codUsuario=None, nombre=None, apellido=None, correo=None, usuario=None, activo=None):
        # Construccion de query
        query = db.session.query(Usuarios)

        # Filtros
        if codUsuario:
            query = query.filter(Usuarios.codUsuario == codUsuario)
        if nombre:
            query = query.filter(Usuarios.nombre.ilike('%'+nombre+'%'))
        if apellido:
            query = query.filter(Usuarios.apellido.ilike('%'+apellido+'%'))
        if correo:
            query = query.filter(Usuarios.correo.ilike('%'+correo+'%'))
        if usuario:
            query = query.filter(Usuarios.usuario.ilike('%'+usuario+'%'))
        if activo != None:
            query = query.filter(Usuarios.activo == activo)

        # Orden
        if orderBy:
            if orderBy == 'nombre':
                query = query.order_by(Usuarios.nombre)
            elif orderBy == 'apellido':
                query = query.order_by(Usuarios.apellido)
            elif orderBy == 'usuario':
                query = query.order_by(Usuarios.usuario)
            elif orderBy == 'activo':
                query = query.order_by(desc(Usuarios.activo))
            else:
                query = query.order_by(Usuarios.nombre)
        else:
            query = query.order_by(Usuarios.nombre)

        return query 