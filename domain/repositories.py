"""Repositories modules"""
from pony import orm
from domain.entities import User
from infrastructure.mongo import document_database

class AllUsers(object):

    @staticmethod
    @orm.db_session
    def find_user_by(**kawrgs):
        return User.get(**kawrgs)

class AllAddresses(object):
    collection = document_database.client.falcon.addresses

    @classmethod
    def find_by(cls, **kwargs):
        address = cls.collection.find_one(kwargs)
        return address
