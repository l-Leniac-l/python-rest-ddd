"""Repositories modules"""
from pony import orm
from domain.entities import User

class AllUsers(object):

    @staticmethod
    @orm.db_session
    def find_user_by(**kawrgs):
        return User.get(**kawrgs)
