""" Start a web server on 0.0.0.0:6543 showing a debug preview. Not intended for production use!

Override host address and port binding with environment variables:

- PREVIEW_HTTP_HOST
- PREVIEW_HTTP_PORT
"""
import logging
from os import environ
from wsgiref.simple_server import make_server

from app import get_application, get_configuration

PREVIEW_HTTP_HOST_DEFAULT = '0.0.0.0'
PREVIEW_HTTP_PORT_DEFAULT = '6543'


def get_debug_preview_config():
    """ Get the default app configuration and update it for debugging and development 
    before starting a simple HTTP server. """
    module_list = ['pyramid_debugtoolbar']
    config = get_configuration()
    for module in module_list:
        include_quietly(config, module)
    return config


def include_quietly(config, module_name):
    try:
        config.include(module_name)
    except ImportError as error:
        logging.warn("Unable to include {} -- Python error: {}".format(module_name, error))


def get_debug_preview_server(port=PREVIEW_HTTP_PORT_DEFAULT, host=PREVIEW_HTTP_HOST_DEFAULT):
    config = get_debug_preview_config()
    wsgi_application = get_application(config)
    return make_server(host, int(port), wsgi_application)


if __name__ == '__main__':
    preview_http_host = environ.get('PREVIEW_HTTP_HOST', PREVIEW_HTTP_HOST_DEFAULT)
    preview_http_port = environ.get('PREVIEW_HTTP_PORT', PREVIEW_HTTP_PORT_DEFAULT)
    server = get_debug_preview_server(port=preview_http_port, host=preview_http_host)
    server.serve_forever()
