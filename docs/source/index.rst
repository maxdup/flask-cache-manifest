Flask-cache-manifest documentation
==================================

.. License
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/maxdup/flask-cache-manifest/blob/master/LICENSE.txt

.. Python Version
.. image:: https://img.shields.io/pypi/pyversions/flask-cache-manifest.svg
   :target: https://pypi.python.org/pypi/flask-cache-manifest/

.. Platforms
.. image:: https://img.shields.io/badge/platform-Linux,_MacOS,_Windows-blue
   :target: https://pypi.python.org/pypi/flask-cache-manifest/

.. Pypi Versions
.. image:: https://badge.fury.io/py/flask-cache-manifest.svg
   :target: https://pypi.python.org/pypi/flask-cache-manifest/

.. CI Status
.. image:: https://github.com/pySourceSDK/flask-cache-manifest/actions/workflows/CI.yml/badge.svg
   :target: https://github.com/pySourceSDK/flask-cache-manifest/actions

.. Covarage
.. image:: coverage.svg

Flask-cache-manifest is a `Flask <https://flask.palletsprojects.com/en/2.2.x/>`_ extension to help you serve your md5 hashed assets via manifest files. Having file hashes in filenames is a popular feature of modern asset bundlers. It's a good strategy for browser cache busting. However, Flask does not provide an easy way to reference those complicated and ever-changing filenames. Flask-cache-manifest lets you reference those assets by leveraging :code:`cache_manifest.json` files.


User Guides
-----------

Get yourself up and running quickly.

.. toctree::
   :maxdepth: 2

   guides

Api Reference
-------------

If you are looking for information on a specific function, class or method, this part of the documentation \
is for you.

.. toctree::
   :maxdepth: 2

   api_ref

Contributing
------------

Few things to know before diving in the code.

.. toctree::
   :maxdepth: 2

   contributing
