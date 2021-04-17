from sqlalchemy import Column, ForeignKey, SmallInteger, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from models import db

class Breadcrumbs(db.Model):
    __tablename__ = 'breadcrumbs'

    codBreadcrumb = Column('cod_breadcrumb', SmallInteger, primary_key=True)
    breadcrumb = Column('breadcrumb', String(20))
    ruta = Column('ruta', String(75))
    anterior = Column('anterior', SmallInteger)