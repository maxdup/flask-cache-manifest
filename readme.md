[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/maxdup/flask-cache-manifest/blob/master/LICENSE.txt)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/flask-cache-manifest.svg)](https://pypi.python.org/pypi/flask-cache-manifest/)
[![PyPI version fury.io](https://badge.fury.io/py/flask-cache-manifest.svg)](https://pypi.python.org/pypi/flask-cache-manifest/)
[![alt text](https://github.com/maxdup/flask-cache-manifest/blob/master/docs/source/coverage.svg "coverage")]()

# Flask-Cache-Manifest

Flask extension serving md5 hashed assets.

Full Documentation:

Turns:
```Jinja
<link type="text/css" rel="stylesheet"
    href="{{ hashed_url_for('static', filename='css/app.css') }}">
```

into

```html
<link type="text/css" rel="stylesheet"
    href="/static/css/app-d41d8cd98f00b204e9800998ecf8427e.css">
```
