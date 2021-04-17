from sqlalchemy import Column, SmallInteger, String
from models import db

class TiposPanal(db.Model):
    __tablename__ = 'tipos_panal'
    __table_args__ = {"schema":"panales"}

    codTipoPanal = Column('cod_tipo_panal', SmallInteger, primary_key=True)
    tipoPanal = Column('tipo_panal', String(2))