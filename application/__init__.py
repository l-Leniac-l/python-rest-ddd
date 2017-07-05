"""Base application module. Used to register services"""
import falcon
from application.status_service import StatusService
from application.user_service import UserService

# Starting falcon API
app = falcon.API()

#Registering services
app.add_route('/', StatusService())
app.add_route('/user/{user_name}', UserService())
