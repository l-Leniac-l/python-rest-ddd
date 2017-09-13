"""Module for app configs"""
import os

class Config(object):
    """Saves all configs as constants"""
    APP_DOCS_URL = '/api_docs.json'
    APP_SWAGGER_URL = '/apidocs'
    APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT')
    APP_RELATIONAL_DATA = os.environ.get('APP_RELATIONAL_DATA')
    APP_RELATIONAL_DATA_HOST = os.environ.get('APP_RELATIONAL_DATA_HOST')
    APP_RELATIONAL_DATA_PORT = os.environ.get('APP_RELATIONAL_DATA_PORT')
    APP_RELATIONAL_DATA_USER = os.environ.get('APP_RELATIONAL_DATA_USER')
    APP_RELATIONAL_DATA_PASSWORD = os.environ.get('APP_RELATIONAL_DATA_PASSWORD')
    APP_RELATIONAL_DATA_DATABASE = os.environ.get('APP_RELATIONAL_DATA_DATABASE')
    APP_DOCUMENT_DATA = os.environ.get('APP_DOCUMENT_DATA')
    APP_DOCUMENT_DATA_HOST = os.environ.get('APP_DOCUMENT_DATA_HOST')
    APP_DOCUMENT_DATA_PORT = os.environ.get('APP_DOCUMENT_DATA_PORT')
    APP_JWT_SECRET = os.environ.get('APP_JWT_SECRET')
    APP_DEBUG_MODE = False

class DevelopmentConfig(Config):
    """Extends the production config"""
    APP_DEBUG_MODE = True

APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT')

CONFIG = Config if APP_ENVIRONMENT == 'production' else DevelopmentConfig
