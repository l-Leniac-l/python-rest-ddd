"""User Service module"""
import falcon
from bson import json_util
from application.base_service import BaseService
from domain.domain_service import DomainService

class AddressService(BaseService):

    def on_get(self, req, resp, user_id):
        address = DomainService.search_user_address(user=int(user_id))
        if address:
            resp.status = falcon.HTTP_200
            resp.body = self.render_template('address.json', address=address)
        else:
            resp.status = falcon.HTTP_404
            resp.body = self.render_status(404, 'No address found!')
