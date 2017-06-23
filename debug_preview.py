# coding=utf-8
""" Start a web server on 0.0.0.0:6543 showing a debug preview. Not intended for production use!

Override host address and port binding with environment variables:

- PREVIEW_HTTP_HOST
- PREVIEW_HTTP_PORT
"""
import logging
from os import environ
from wsgiref.simple_server import make_server

from app import get_application, get_configuration

DEBUG_MODULES = ['pyramid_debugtoolbar']

PREVIEW_HTTP_HOST_DEFAULT = '0.0.0.0'
PREVIEW_HTTP_PORT_DEFAULT = '6543'


def get_debug_preview_config():
    """ Get the default app configuration and update it for debugging and development 
    before starting a simple HTTP server. """
    config = get_configuration()
    for possible_module in DEBUG_MODULES:
        try_include(config, possible_module)
    return config


def try_include(config, module_name):
    """
    If possible, include a Python module as a Pyramid extension. Errors are logged instead of halting.
    
    :param config: 
    :param module_name: 
    """
    try:
        config.include(module_name)
    except ImportError as error:
        logging.warn(f"Unable to include {module_name} -- Python error: {error}")


def get_debug_preview_server(port=PREVIEW_HTTP_PORT_DEFAULT, host=PREVIEW_HTTP_HOST_DEFAULT):
    """
    Configure the app for debug/development mode and create a WSGI server object.
    :param port: 
    :param host: 
    :return: 
    """
    config = get_debug_preview_config()
    wsgi_application = get_application(config)
    return make_server(host, int(port), wsgi_application)


if __name__ == '__main__':
    preview_http_host = environ.get('PREVIEW_HTTP_HOST', PREVIEW_HTTP_HOST_DEFAULT)
    preview_http_port = environ.get('PREVIEW_HTTP_PORT', PREVIEW_HTTP_PORT_DEFAULT)
    server = get_debug_preview_server(port=preview_http_port, host=preview_http_host)
    print(f'Starting HTTP server listening on {preview_http_host}:{preview_http_port}…')
    server.serve_forever()
