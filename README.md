# *Slimgen-CLI* (provisional project name)

A "hello world" web app, developed for use as a [12-factor application].
Web page templates in the app use a variant of [Slim].

## Roadmap

- Markdown support for text nodes in the templates
- YAML data for the template context
- command line interface for static file generation
- deploy to Amazon Web Services S3 bucket
- more Python compatibility

## Installation

### Requirements

- [Docker]

#### Build Docker image

Instead of "installing" from source, directly to your host system, Docker
will provide the appropriate server system in a container so the project's
runtime environment stays cleanly isolated and reliably deterministic.

- Build the Docker image like so, with `my_image_name` being one of your
own choosing:

```bash
docker build -t my_image_name .
```

Now it's ready to run.

**WARNING**: It's easy to forget that this building of the image takes
a snapshot of the source code at the time when the build command is run,
and therefore newer versions of the project will need a fresh build to
take an updated snapshot. (You can re-use the image name you chose,
thereby replacing the image, or select a new one each time so you can
keep old versions handy.)

## Production Usage

- Create and start a container based on the previously built image, again
using the image name you chose when building:

```bash
docker run --rm -p 80:80 my_image_name
```

- Browse to your host IP address to access the app, or http://localhost/.
- Log messages will print to the screen unless your Docker system was
configured to handle logging in a non-default manner.
- To stop and remove the container, press `^C` (Control+C).

**TIP:** You can supply an IP address and port number of your own choosing
in place of `80:80`. For example, `127.0.0.1:8080:80`. See the [Docker run reference] for details.

**TIP:** You can use `-d` instead of `--rm` if you want the container to
run in the background, without printing log messages automatically to
the screen. If you do so, you will have to manage your container as usual
with the [Docker commands], or a Docker GUI such as [Kitematic] or
[PyCharm's built-in Docker support].

### Logging

- Messages from the application and the bundled uWSGI server stream to the
container logs.
- By default, the container streams to standard output.
You can configure [Docker logging drivers] to handle those messages
however you like.

## Development

### Requirements

- Python 3.6+ (other versions not tested)
  - pip
  - virtualenv

### Python development setup

It's highly recommended that you create a virtual environment for Python
packages, like so:

```bash
virtualenv venv
```

Before attempting to run the project, install the required packages in
the virtual environment, like so:

```bash
venv/bin/pip install -r requirements.txt
```

During devolopment, if you add Python packages dependencies, update
[`requirements.txt`] and re-run the `pip install` command as shown above.

### Running the preview server

**WARNING:** The preview server is not very suitable for production use, especially
because the debug mode views will be activated, and the Pyramid debug toolbar
may be loaded, all of which increase security vulnerabilities.

```bash
venv/bin/python debug_preview.py
```

By default, the HTTP server will start listening on 0.0.0.0:6543. You
can override the host address and port number binding by setting these
environment variables in the shell that executes `debug_preview.py`:

- PREVIEW_HTTP_HOST
- PREVIEW_HTTP_PORT

This can be done inline if you're using a common Linux/Unix shell,
such as Bash:

```bash
PREVIEW_HTTP_HOST=127.0.0.1 PREVIEW_HTTP_PORT=8080 venv/bin/python debug_preview.py
```

If you use an IDE such as PyCharm, you can edit these variables into a
[run configuration]. This works in *Community Edition* as well as
*Professional Edition*.

**TIP:** *PyCharm Professional Edition* has a [Pyramid server]
run configuration preset which expects a `.ini` file for each deployment
configuration, so if you really want, you can create a `development.ini`.
However, there's no significant benefit to this approach and environment
variables work just as well in most cases—and are more conducive to 12-factor
app development—so such a file hasn't been included in the code base.

[12-factor application]: https://12factor.net/
[Docker logging drivers]: https://docs.docker.com/engine/admin/logging/overview/
[Docker]: https://docs.docker.com/engine/installation/
[Slim]: https://github.com/thoughtnirvana/slimish-jinja2
[run configuration]: https://www.jetbrains.com/help/pycharm/run-debug-configuration-python.html
[Pyramid Server]: https://www.jetbrains.com/help/pycharm/run-debug-configuration-pyramid-server.html
[`requirements.txt`]: https://pip.pypa.io/en/stable/user_guide/#requirements-files
[Docker commands]: https://docs.docker.com/engine/reference/commandline/docker/
[PyCharm's built-in Docker support]: https://www.jetbrains.com/help/pycharm/docker.html
[Kitematic]: https://docs.docker.com/kitematic/userguide/
[Docker run reference]: https://docs.docker.com/engine/reference/run/#expose-incoming-ports
