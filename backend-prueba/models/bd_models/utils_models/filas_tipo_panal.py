from sqlalchemy import Column, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import db

class FilasTipoPanal(db.Model):
    __tablename__ = 'filas_tipo_panal'
    __table_args__ = {"schema":"panales"}

    codFilaTipoPanal = Column('cod_fila_tipo_panal', SmallInteger, primary_key=True)
    tipoPanalCod = Column('tipo_panal_cod', SmallInteger)
    filaTipoPanal = Column('fila_tipo_panal', SmallInteger)
    userAt = Column('user_at', SmallInteger)


    def listQuery(tipoPanalCod=None):
        # Construccion de query
        query = db.session.query(FilasTipoPanal)

        # Filtros
        if tipoPanalCod:
            query = query.filter(FilasTipoPanal.tipoPanalCod == tipoPanalCod)

        query = query.order_by(FilasTipoPanal.filaTipoPanal)

        return query