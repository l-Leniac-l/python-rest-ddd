"""Module for app configs"""
import os

class Config(object):
    """Saves all configs as constants"""
    APP_DOCS_URL = '/api_docs.json'
    APP_SWAGGER_URL = '/apidocs'
    APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT')
    APP_DB_HOST = os.environ.get('APP_DB_HOST')
    APP_DB_PORT = os.environ.get('APP_DB_PORT')
    APP_DB_USER = os.environ.get('APP_DB_USER')
    APP_DB_PASSWORD = os.environ.get('APP_DB_PASSWORD')
    APP_DB_DATABASE = os.environ.get('APP_DB_DATABASE')
    APP_JWT_SECRET = os.environ.get('APP_JWT_SECRET')
    APP_DEBUG_MODE = False

class DevelopmentConfig(Config):
    """Extends the production config"""
    APP_DEBUG_MODE = True

APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT')

CONFIG = Config if APP_ENVIRONMENT == 'production' else DevelopmentConfig
