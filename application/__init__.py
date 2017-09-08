"""Base application module. Used to register services"""
import falcon
import dependency_injector.providers as providers
from falcon_swagger_ui import register_swaggerui_app
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from application.environments.config import CONFIG
from application.service_register import ServiceRegister

class Application(object):
    """Application starter class"""
    def __init__(self):
        self.app_config = providers.Singleton(CONFIG)

        self.user_loader = lambda user: user
        self.jwt_auth = JWTAuthBackend(self.user_loader,
                                       self.app_config().APP_JWT_SECRET,
                                       algorithm='HS256',
                                       auth_header_prefix='Bearer',
                                       audience='localhost:5000',
                                       required_claims=['exp'])
        self.auth_middleware = FalconAuthMiddleware(self.jwt_auth,
                                                    exempt_routes=[
                                                        self.app_config().APP_SWAGGER_URL,
                                                        self.app_config().APP_DOCS_URL
                                                    ])
        self.app = falcon.API(middleware=[self.auth_middleware])

        self.start()

    def start(self):
        ServiceRegister.register_services(self.app)
        register_swaggerui_app(self.app,
                               self.app_config().APP_SWAGGER_URL,
                               self.app_config().APP_DOCS_URL,
                               config={
                                   'supportedSubmitMethods': ['get'],
                               })

app = Application()
