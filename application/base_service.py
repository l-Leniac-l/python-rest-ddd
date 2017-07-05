"""Base service"""
from jinja2 import Environment, PackageLoader

class BaseService(object):
    def __init__(self):
        self.env = Environment(loader=PackageLoader('application', 'templates'))

    def render_template(self, name, **kwargs):
        """Render the given @name template and gives args to it"""
        template = self.env.get_template(name)
        return template.render(**kwargs)

    def render_status(self, code, message):
        """Render a response status"""
        template = self.env.get_template('status.json')
        return template.render(code=code, message=message)
