"""Relational database module"""
import dependency_injector.providers as providers
from pony import orm
from application.environments.config import CONFIG

class Database(object):
    def __init__(self):
        self.app_config = providers.Singleton(CONFIG)
        self.db = orm.Database()
        self.db.bind(self.app_config().APP_RELATIONAL_DATA,
                     host=self.app_config().APP_RELATIONAL_DATA_HOST,
                     port=int(self.app_config().APP_RELATIONAL_DATA_PORT),
                     user=self.app_config().APP_RELATIONAL_DATA_USER,
                     passwd=self.app_config().APP_RELATIONAL_DATA_PASSWORD,
                     db=self.app_config().APP_RELATIONAL_DATA_DATABASE)

relational_database = Database()
