from pyramid.config import Configurator

from app.view import respond_hello_world


def get_configuration():
    """ Instantiate a Configurator object and apply this app's configuration to it. """
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(respond_hello_world, route_name='hello')
    return config


def get_application(config=None):
    """ Apply the given config or default config to a new application object. """
    if config is None:
        config = get_configuration()
    wsgi_app = config.make_wsgi_app()
    return wsgi_app
