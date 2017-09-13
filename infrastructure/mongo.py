"""Document database module"""
import dependency_injector.providers as providers
from pymongo import MongoClient
from application.environments.config import CONFIG

class Database(object):
    def __init__(self):
        self.app_config = providers.Singleton(CONFIG)
        self.client = MongoClient('{0}://{1}:{2}/'.format(self.app_config().APP_DOCUMENT_DATA,
                                                          self.app_config().APP_DOCUMENT_DATA_HOST,
                                                          self.app_config().APP_DOCUMENT_DATA_PORT))

document_database = Database()
