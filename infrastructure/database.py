"""Database module"""
import dependency_injector.providers as providers
from pony import orm
from application.environments.config import CONFIG

class Database(object):
    def __init__(self):
        self.app_config = providers.Singleton(CONFIG)
        self.db = orm.Database()
        self.db.bind('mysql',
                     host=self.app_config().APP_DB_HOST,
                     port=int(self.app_config().APP_DB_PORT),
                     user=self.app_config().APP_DB_USER,
                     passwd=self.app_config().APP_DB_PASSWORD,
                     db=self.app_config().APP_DB_DATABASE)

database = Database()
