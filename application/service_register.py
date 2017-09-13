"""Service Register"""
from application.status_service import StatusService
from application.user_service import UserService
from application.spec_service import SpecService
from application.address_service import AddressService

class ServiceRegister(object):

    @staticmethod
    def register_services(app):
        app.add_route('/', StatusService())
        app.add_route('/user/{user_name}', UserService())
        app.add_route('/address/{user_id}', AddressService())

        app.add_route('/api_docs.json', SpecService())
