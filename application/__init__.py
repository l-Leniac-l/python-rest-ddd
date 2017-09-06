"""Base application module. Used to register services"""
import falcon
from falcon_swagger_ui import register_swaggerui_app
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from application.service_register import ServiceRegister

class Application(object):
    """Application starter class"""

    SWAGGER_URL = '/apidocs'
    API_URL = '/api_docs.json'

    def __init__(self, jwt_auth):
        self.auth_middleware = FalconAuthMiddleware(jwt_auth,
                                                    exempt_routes=['/apidocs'])
        self.app = falcon.API(middleware=[self.auth_middleware])

        self.start()

    def start(self):
        ServiceRegister.register_services(self.app)
        register_swaggerui_app(self.app, self.SWAGGER_URL, self.API_URL, config={
            'supportedSubmitMethods': ['get'],
        })

user_loader = lambda user: user

jwt_auth_ = JWTAuthBackend(user_loader,
                           'qwertyuiopasdfghjklzxcvbnm123456',
                           algorithm='HS256',
                           auth_header_prefix='Bearer',
                           audience='localhost:5000',
                           required_claims=['exp'])

app = Application(jwt_auth_)
