# coding=utf-8
"""Application entrypoint and bootstrap. Loads configuration, imports add-on
 modules and creates a WSGI application object."""
from .core import get_configuration


def get_application(config=None):
    """ Apply the given config or default config to a new WSGI application object. """
    if config is None:
        config = get_configuration()
    wsgi_app = config.make_wsgi_app()
    return wsgi_app
