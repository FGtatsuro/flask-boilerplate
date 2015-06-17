|Build Status|

Flask-Boilerplate
=================

A Paste template for Flask application.

Requirement
-----------

-  PasteScript

Create a boilerplate of Flask application
-----------------------------------------

To create a boilerplate, you run ``paster create`` command as follows.

.. code:: bash

    $ paster create --list-template
    Available templates:
      basic_package:      A basic setuptools-enabled package
      flask_boilerplate:  A boilerplate for Flask project
      paste_deploy:       A web application deployed through paste.deploy

    $ paster create --template=flask_boilerplate test_project
    Selected and implied templates:
      Flask-Boilerplate#flask_boilerplate  A boilerplate for Flask project

    Variables:
      egg:      test_project
      package:  test_project
      project:  test_project
    Enter app_name (Flask application name): app
    Enter description (One-line description of the package) ['']: Test application
    Enter author (Author name) ['']:
    Enter author_email (Author email) ['']:
    ...

    $ ls test_project
    LICENSE               README.rst            requirements.txt      setup.cfg             tests
    MANIFEST.in           app                   run.py                setup.py              tox.ini
    Procfile              config.ini            runtime.txt           test_project.egg-info uwsgi.ini

Develop this project
--------------------

First, please resolve dependencies of this project.

.. code:: bash

    $ pip install -r requirements.txt

After some fix, please run tests.

.. code:: bash

    $ tox
    # or
    $ python setup.py test

.. |Build Status| image:: https://travis-ci.org/FGtatsuro/flask-boilerplate.svg?branch=master
   :target: https://travis-ci.org/FGtatsuro/flask-boilerplate
