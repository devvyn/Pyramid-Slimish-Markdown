FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
EXPOSE 80

RUN pip install virtualenv
RUN virtualenv venv
RUN /usr/src/app/venv/bin/pip install --no-cache-dir uwsgi

COPY wsgi.py /usr/src/app/
COPY requirements.txt /usr/src/app/
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY app/ /usr/src/app/app/

CMD ["/usr/src/app/venv/bin/uwsgi","-w","wsgi","-H","venv","--http",":80"]
