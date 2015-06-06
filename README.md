[![Build Status](https://travis-ci.org/FGtatsuro/flask-boilerplate.svg?branch=master)](https://travis-ci.org/FGtatsuro/flask-boilerplate)

Flask-Boilerplate
=================

A Paste template for Flask application.

Requirement
-----------

- PasteScript

Create a boilerplate of Flask application
-----------------------------------------

To create a boilerplate, you run `paster create` command as follows.

```bash
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

$ ls -R test_project
LICENSE               Procfile              app                   requirements.txt      runtime.txt           test_project.egg-info tox.ini
MANIFEST.in           README.md             config.py             run.py                setup.py              tests

test_project/app:
__init__.py models.py   static      templates   views.py

test_project/app/static:
css js

test_project/app/static/css:
style.css

test_project/app/static/js:
main.js

test_project/app/templates:
index.html  items.html  layout.html utils.html

test_project/test_project.egg-info:
PKG-INFO             SOURCES.txt          dependency_links.txt entry_points.txt     not-zip-safe         requires.txt         top_level.txt

test_project/tests:
test_smoke.py
```

Develop this project
--------------------

First, please resolve dependencies of this project.

```bash
$ pip install -r requirements.txt
```

After some fix, please run tests.

```bash
$ tox
# or
$ python setup.py test
```
