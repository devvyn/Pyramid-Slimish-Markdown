# coding=utf-8
""" Essential web interface module """

from pyramid.config import Configurator

from .view import respond_hello_world


def apply_routes(config):
    """
Add routes and views to the Configurator instance.
    :param config: 
    """
    config.add_route('hello', '/')
    config.add_view(respond_hello_world, route_name='hello')
    # @todo convert to declarative configuration using decorators in plug-able modules


def get_configuration():
    """ Instantiate a Configurator object and apply this app's configuration to it. """
    config = Configurator()
    apply_renderers(config)
    apply_routes(config)
    return config


def apply_renderers(config):
    config.include('pyramid_jinja2')
