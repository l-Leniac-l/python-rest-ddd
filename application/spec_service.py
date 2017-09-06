"""Status Service to tell if the application is running or not"""

import falcon
from application.base_service import BaseService

class SpecService(BaseService):

    auth = {
        'auth_disabled': True
    }

    def on_get(self, req, resp): # pylint: disable=unused-argument
        resp.status = falcon.HTTP_200
        resp.body = self.render_specs()
