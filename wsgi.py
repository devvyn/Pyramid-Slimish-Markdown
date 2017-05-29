""" WSGI entry point at `application` """
from app import get_wsgi_application

application = get_wsgi_application()
