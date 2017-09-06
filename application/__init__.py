"""Base application module. Used to register services"""
import falcon
from falcon_swagger_ui import register_swaggerui_app
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from application.service_register import ServiceRegister

# Defining documentation specs
SWAGGER_URL = '/apidocs'
API_URL = '/api_docs.json'

user_loader = lambda user: user
# Defining JWT configs
#sample jwt
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE1MDQ2NjUwMTQsImV4cCI6MTUzNjI4NzQxNCwiYXVkIjoibG9jYWxob3N0OjUwMDAiLCJzdWIiOiJsZW5pbHNvbi4xMDBAZ21haWwuY29tIiwiTmFtZSI6Ikxlbmlsc29uIiwiRW1haWwiOiJsZW5pbHNvbi4xMDBAZ21haWwuY29tIiwiUm9sZSI6IlByb2plY3QgQWRtaW5pc3RyYXRvciJ9.a2StPd8pY7-vlgDtXCTRPHaBWga7ceOMLpBZnlvkJY8
jwt_auth = JWTAuthBackend(user_loader,
                          'qwertyuiopasdfghjklzxcvbnm123456',
                          algorithm='HS256',
                          auth_header_prefix='Bearer',
                          audience='localhost:5000',
                          required_claims=['exp'])
auth_middleware = FalconAuthMiddleware(jwt_auth)
# Starting falcon API
app = falcon.API(middleware=[auth_middleware])

ServiceRegister.register_services(app)

register_swaggerui_app(app, SWAGGER_URL, API_URL, config={
    'supportedSubmitMethods': ['get'],
})
