# Hello World (Slim)

## [v0.1.1]

### Added

Initial project starter, a hello world web page.

- Simple Pyramid project in `app.core`, exposed through `app`
- `debug_preview.py` - starts web server in debug mode
    - support for config via env var (see Readme)
- `Dockerfile` - serves app on port 80 via uwsgi for production
- `requirements.txt` - dependencies for pip to install
- `wsgi.py` - contains entry point for uwsgi

[Unreleased]: https://gitlab.com/devvyn/slimgen-CLI/compare/v0.1.0...master
[v0.1.0]: https://gitlab.com/devvyn/slimgen-CLI/tree/v0.1.0
