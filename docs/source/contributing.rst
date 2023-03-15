Contributing
============

Few things to know before diving in the code.


Project Guidelines
------------------

#. Be pythonic
#. Document your code
#. Test your code

That is all.


Dev Environment
---------------

To tinker with the code, it's recommended that you install the library from the cloned folder with:

.. code-block:: bash

   pip install --editable .


This will allow you to import Flask-cache-manifest in other projects directly while being able to edit the extension directly from the git folder. This way, you can make sure Flask-cache-manifest will work as intended in the context of your own project.


Documenting
-----------
The documentation is done with `Sphinx <http://www.sphinx-doc.org/en/master/>`_.
To build the Sphinx documentation, you need:

.. code-block:: bash

    pip install -U sphinx
    pip install sphinx-autobuild

Then you can run sphinx-autobuild.sh in the docs/ directory. The documentation pages will be served on http://127.0.0.1:8000 by default.


Testing
-------
Tests are ran using pytest. Pytest is included in the :code:`requirements.txt` file. make sure those are installed and you'll be good to go.

.. code-block:: bash

    pytest


If you have a more elaborate setup with tox and pyenv, you'll have access to a few more automations by running tox.

.. code-block:: bash

    tox # to run the full test suite
    tox -e py37 # to test a specific environment
    tox -e docs # to build the documentation
