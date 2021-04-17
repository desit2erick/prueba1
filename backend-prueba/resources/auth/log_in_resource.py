from flask_jwt_extended.view_decorators import jwt_required
from flask_restx import Resource, fields, fields, reqparse, marshal, Namespace
from cryptography.fernet import Fernet
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt_claims
from models import db, Usuarios, Roles, RolesPermisos, UsuariosRoles, messageHandler
from utils import cargarBitacora
import settings, datetime

login = Namespace('login')

loginFields = {
    'token': fields.String,
    'expires': fields.String
}

loginRequest = login.model('Login', {
    'usuario': fields.String,
    'password': fields.String
})

tiempoExpiracion = 60

@login.route('')
class LogInResource(Resource):

    def __init__(self, api, *args, **kwargs):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('usuario')
        self.reqparse.add_argument('password')
        super().__init__(api=api, *args, **kwargs)

    @jwt_required
    def get(self):
        try:
            expires = datetime.timedelta(minutes=tiempoExpiracion)
            token = create_access_token(identity=get_jwt_identity(), expires_delta=expires, user_claims=get_jwt_claims())
            date = datetime.datetime.today() + expires
            return marshal({'token': token, 'expires': str(date)}, loginFields), 200
        except:
            return messageHandler('Error al crear token')

    @login.doc(body=loginRequest, params={'nombre':''})
    def post(self):
        args = self.reqparse.parse_args()
        usr: Usuarios = db.session.query(Usuarios).filter_by(
            usuario=str(args['usuario'])).first()
        if usr == None:
            return messageHandler('Usuario incorrecto',401)
        if not usr.activo:
            return messageHandler('Usuario deshabilitado',401)
        f = Fernet(settings.CRYPTO_SECRET_KEY)
        if f.decrypt(usr.password.encode()).decode() == str(args['password']):
            try:
                permisos = self.getPermisos(usr.codUsuario)
                nombre = usr.nombre + ' ' + usr.apellido
                claims = { 'permisos': permisos, 'nombre': nombre }
                expires = datetime.timedelta(minutes=tiempoExpiracion)
                token = create_access_token(
                    identity=usr.codUsuario, expires_delta=expires, user_claims=claims)
                date = datetime.datetime.today() + expires
            except:
                return messageHandler('Error al crear token')
            cargarBitacora(usr, 'Inicio de sesión', 'Usuario: {0}'.format(usr.usuario))
            return marshal({'token': token, 'expires': str(date)}, loginFields), 200
        else:
            return messageHandler('Contraseña incorrecta', 401)

    def getPermisos(self, codUsuario):
        rolesUsuario = db.session.query(UsuariosRoles).filter(UsuariosRoles.usuarioCod == codUsuario, UsuariosRoles.activo).all()
        permisos = []
        for rolUsuario in rolesUsuario:
            rol: Roles = rolUsuario.rol
            if rol.activo:
                permiso: RolesPermisos
                for permiso in rol.rolesPermisos:
                    if permiso.permisoCod not in permisos and permiso.activo:
                        permisos.append(permiso.permisoCod)
        return permisos