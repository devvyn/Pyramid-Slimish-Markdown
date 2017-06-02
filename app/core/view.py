from pyramid.renderers import render_to_response


def respond_hello_world(request):
    print('Incoming request')
    response = render_to_response('template/hello.html.jinja2', {}, request=request)
    return response
