Quickstart
==========

Get yourself up and running quickly.

Installation
------------

PyPI
~~~~
flask-cache-manifest is available on the Python Package Index. This makes installing it with pip as easy as:

.. code-block:: bash

   pip install flask-cache-manifest

Git
~~~

If you want the latest code or even feel like contributing, the code is available on GitHub.

You can easily clone the code with git:

.. code-block:: bash

   git clone git://github.com/maxdup/flask-cache-manifest.git

and install it from the repo directory with:

.. code-block:: bash

   python setup.py install
   # or
   pip install .


Initializing
------------

The extension needs to be loaded alongside your Flask application.

Here's how it's done:

.. code-block:: python

    from flask import Flask, Blueprint
    from flask_cache_manifest import FlaskCacheManifest

    flaskCacheManifest = FlaskCacheManifest()

    app = Flask('my-app',
                static_folder='dist/static',
                static_url_path='/static')

    bp = Blueprint('my-blueprint',
                   __name__,
                   static_folder='blueprints/static',
                   static_url_path='/bp/static')

    app.register_blueprint(bp)

    flaskCacheManifest.init_app(app)

    app.run()

.. note::
    Ideally, :func:`flaskCacheManifest.init_app` needs to be called after you've registered your blueprints.
    Static folders registered after :func:`init_app<flaskCacheManifest.init_app>` will not be loaded.


Usage
-----

Flask-cache-manifest adds the :any:`hashed_url_for` function for use in your templates.
It is analogous to Flask's url_for. Given the above example and its blueprints,
here's how you would be able to reference your static files in your Jinja templates.

.. code-block:: html

    <!-- from the app's static folder -->
    <link type="text/css" rel="stylesheet"
        href="{{ hashed_url_for('static', filename='css/app.css') }}">

    <!-- from the blueprint's static folder -->
    <link type="text/css" rel="stylesheet"
        href="{{ hashed_url_for('my-blueprint.static', filename='css/app.css') }}">

    <!-- from the static folder relative to what is currently being rendered -->
    <link type="text/css" rel="stylesheet"
        href="{{ hashed_url_for('.static', filename='css/app.css') }}">
