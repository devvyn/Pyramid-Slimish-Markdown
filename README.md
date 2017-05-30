A hello world web app, developed for use as a [12-factor application](https://12factor.net).

## Installation

### Docker

#### Requirements

- docker

#### Build Docker image

```bash
docker build -t my_image_name .
```

## Usage

#### Run Docker image

```bash
docker run --rm -p 80:80 my_image_name
```

Browse to your host IP address to access the app, or http://localhost/.

Messages from the application and the bundled uWSGI server stream to the
container logs. You can configure your Docker command to handle those
messages however you like. By default, the messages stream to
standard output from the container.

## Development

### Requirements

- python
- pip
- virtualenv

### Setup

```bash
virtualenv venv
venv/bin/pip install -r requirements.txt
```

If you want to add dependencies, update `requirements.txt`
 and re-run the `pip install` command from the virtual environment:

```bash
venv/bin/pip install -r requirements.txt
```

### Running the preview server

```bash
venv/bin/python serve.py
```