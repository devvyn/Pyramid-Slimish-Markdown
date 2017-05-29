""" Start a web server on 0.0.0.0:6543 showing a debug preview. Not intended for production use!

Override host address and port binding with environment variables:

- PREVIEW_HTTP_HOST
- PREVIEW_HTTP_PORT
"""
import logging
from os import environ
from wsgiref.simple_server import make_server

from app import get_wsgi_application, get_app_config

PREVIEW_HTTP_HOST_DEFAULT = '0.0.0.0'
PREVIEW_HTTP_PORT_DEFAULT = 6543


def get_debug_preview_config():
    """ Get the default app configuration and update it for debugging and development 
    before starting a simple HTTP server. """
    config = get_app_config()
    debug_module_name = 'pyramid_debugtoolbar'
    try:
        config.include(debug_module_name)
    except ImportError as error:
        logging.warn("{} - This app is running in development mode, and may be insecure. "
                     "If you want to use the web based debugging tools, install the "
                     "`{}` module.".format(error, debug_module_name))
    return config


def get_debug_preview_server(port=PREVIEW_HTTP_PORT_DEFAULT, host=PREVIEW_HTTP_HOST_DEFAULT):
    config = get_debug_preview_config()
    wsgi_application = get_wsgi_application(config)
    return make_server(host, port, wsgi_application)


if __name__ == '__main__':
    http_host = environ.get('PREVIEW_HTTP_HOST', PREVIEW_HTTP_HOST_DEFAULT)
    http_port = environ.get('PREVIEW_HTTP_PORT', PREVIEW_HTTP_PORT_DEFAULT)
    get_debug_preview_server(port=http_port, host=http_host).serve_forever()
