""" Application entrypoint """
from .core import get_configuration

__all__ = ['get_application']


def get_application(config=None):
    """ Apply the given config or default config to a new WSGI application object. """
    if config is None:
        config = get_configuration()
    wsgi_app = config.make_wsgi_app()
    return wsgi_app
