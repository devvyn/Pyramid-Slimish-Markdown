# Hello World (Slim)

## [v0.1.1]

### Changed

- minor fix in `CHANGELOG.md` so GitLab.com displays link correctly

## [v0.1.0]

### Added

Initial project starter, a hello world web page.

- Simple Pyramid project in `app.core`, exposed through `app`
- `debug_preview.py` - starts web server in debug mode
    - support for config via env var (see Readme)
- `Dockerfile` - serves app on port 80 via uwsgi for production
- `requirements.txt` - dependencies for pip to install
- `wsgi.py` - contains entry point for uwsgi

[Unreleased]: https://github.com/devvyn/Pyramid-Slimish-Markdown/compare/v0.1.1...master
[v0.1.1]: https://github.com/devvyn/Pyramid-Slimish-Markdown/compare/v0.1.0...v0.1.1
[v0.1.0]: https://github.com/devvyn/Pyramid-Slimish-Markdown/tree/v0.1.0
