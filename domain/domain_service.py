"""Domain Service Module"""
from domain.repositories import AllUsers

class DomainService(object):

    @staticmethod
    def search_user_data(**kwargs):
        return AllUsers.find_user_by(**kwargs)
