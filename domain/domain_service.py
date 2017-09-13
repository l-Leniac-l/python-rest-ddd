"""Domain Service Module"""
from domain.repositories import AllUsers, AllAddresses

class DomainService(object):

    @staticmethod
    def search_user_data(**kwargs):
        return AllUsers.find_user_by(**kwargs)

    @staticmethod
    def search_user_address(**kwargs):
        return AllAddresses.find_by(**kwargs)
