from sqlalchemy import Column, ForeignKey, SmallInteger, Boolean, TIMESTAMP, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import desc
from models import db


class RolesPermisos(db.Model):
    __tablename__ = 'roles_permisos'
    __table_args__ = {"schema":"seguridad"}

    codRolPermiso = Column('cod_rol_permiso', SmallInteger, primary_key=True)
    rolCod = Column('rol_cod', SmallInteger, ForeignKey('seguridad.roles.cod_rol'))
    permisoCod = Column('permiso_cod', SmallInteger, ForeignKey('seguridad.permisos.cod_permiso'))
    create = Column('create', TIMESTAMP)
    update = Column('update', TIMESTAMP)
    delete = Column('delete', TIMESTAMP)
    userAt = Column('user_at', SmallInteger)
    activo = Column('activo', Boolean)

    permisos = relationship('Permisos', backref=backref('RolesPermisos', lazy='select'))
    roles = relationship('Roles', backref=backref('RolesPermisos', lazy='select'))

    def listQuery(orderBy=None, codRolPermiso=None, rolCod=None, permisoCod=None, activo=None):
        # Construccion de query
        query = db.session.query(RolesPermisos)

        # Filtros
        if codRolPermiso:
            query = query.filter(RolesPermisos.codRolPermiso == codRolPermiso)
        if rolCod:
            query = query.filter(RolesPermisos.rolCod == rolCod)
        if permisoCod:
            query = query.filter(RolesPermisos.permisoCod == permisoCod)
        if activo != None:
            query = query.filter(RolesPermisos.activo == activo)

        # Orden
        if orderBy:
            if orderBy == 'codRolPermiso':
                query = query.order_by(RolesPermisos.codRolPermiso)
            elif orderBy == 'rolCod':
                query = query.order_by(desc(RolesPermisos.rolCod))
            elif orderBy == 'permisoCod':
                query = query.order_by(desc(RolesPermisos.permisoCod))
            elif orderBy == 'activo':
                query = query.order_by(desc(RolesPermisos.activo))
            else:
                query = query.order_by(RolesPermisos.codRolPermiso)
        else:
            query = query.order_by(RolesPermisos.codRolPermiso)

        return query
