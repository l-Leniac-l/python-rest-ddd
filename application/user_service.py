"""User Service module"""
import falcon
from application.base_service import BaseService
from domain.domain_service import DomainService

class UserService(BaseService):

    def on_get(self, req, resp, user_name): # pylint: disable=unused-argument
        user = DomainService.search_user_data(user_name=user_name)
        if user:
            resp.status = falcon.HTTP_200
            resp.body = self.render_template('user.json', user=user)
        else:
            resp.status = falcon.HTTP_404
            resp.body = self.render_status(404, 'No user found!')
