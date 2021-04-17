from os import environ
from .settings import *

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CRYPTO_SECRET_KEY = b'pULlI0deoTPEear72Uy-I8LEYL0oPvZu9fS6fDphR1s='

class Config(object):
    PROPAGATE_EXCEPTIONS = True
    RESTX_MASK_SWAGGER = False
    JWT_SECRET_KEY = 'RLT03-punto-venta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:pZ2HiBhc@10.10.1.8:5432/db_dev_grc'
    UPLOAD_FOLDER = '//10.10.1.7/system/dev'
    SAP_RLT_USER = ['PRUEBA_RLT', 'manager', 'SBman.20']
    SAP_FARINCA_USER = ['PRUEBA_FARINCA', 'manager', 'SBman.20']
    DEBUG = True

class StageConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:pZ2HiBhc@10.10.1.8:5432/db_dev_grc'
    UPLOAD_FOLDER = '/home/admin/storage/dev'
    SAP_RLT_USER = ['PRUEBA_RLT', 'manager', 'SBman.20']
    SAP_FARINCA_USER = ['PRUEBA_FARINCA', 'manager', 'SBman.20']
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:pZ2HiBhc@10.10.1.8:5432/db_prod_grc'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = '/home/admin/storage/prod'
    SAP_RLT_USER = ['SBO_LIVE_RLT', 'manager', 'SBman.20']
    SAP_FARINCA_USER = ['SBO_LIVE_FARINCA', 'manager', 'SBman.20']
    DEBUG = False