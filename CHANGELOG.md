# pyramid-starter-12-factor

## [Unreleased]

### Added

Initial project starter, a hello world web page.

#### Project

- `LICENSE.txt`
- `README.md`
- `app` package

#### Development

- `.gitignore`
- `debug_preview.py` - starts web server

#### Build

- `Dockerfile` - serves app on port 80 via uwsgi
- `requirements.txt` - dependencies for pip to install
- `wsgi.py` - contains entry point for uwsgi
  (used by the Docker container)


[Unreleased]: #