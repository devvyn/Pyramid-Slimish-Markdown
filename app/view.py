from pyramid.response import Response


def respond_hello_world(*_):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')