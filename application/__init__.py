"""Base application module. Used to register services"""
import falcon
from application.status_service import StatusService
from application.user_service import UserService
from application.spec_service import SpecService
from falcon_swagger_ui import register_swaggerui_app

# Defining documentation specs
SWAGGER_URL = '/apidocs'
API_URL = '/api_docs.json'
# Starting falcon API
app = falcon.API()

# Registering services
app.add_route('/', StatusService())
app.add_route('/user/{user_name}', UserService())
app.add_route('/api_docs.json', SpecService())

register_swaggerui_app(app, SWAGGER_URL, API_URL, config={
    'supportedSubmitMethods': ['get'],
})
