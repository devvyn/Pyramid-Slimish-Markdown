FROM python:2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY serve.py /usr/src/app/

cmd ["/usr/local/bin/python","/usr/src/app/serve.py"]
