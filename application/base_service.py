"""Base service"""
import json
import yaml
from jinja2 import Environment, PackageLoader

class BaseService(object):
    def __init__(self):
        self.env = Environment(loader=PackageLoader('application', 'templates'))
        self.spec_env = Environment(loader=PackageLoader('application', 'specs'))

    def render_specs(self):
        template = self.spec_env.get_template('default.yml')
        rendered = template.render()
        return json.dumps(yaml.load(rendered))

    def render_template(self, name, **kwargs):
        """Render the given @name template and gives args to it"""
        template = self.env.get_template(name)
        return template.render(**kwargs)

    def render_status(self, code, message):
        """Render a response status"""
        template = self.env.get_template('status.json')
        return template.render(code=code, message=message)
