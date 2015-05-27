[![Build Status](https://travis-ci.org/FGtatsuro/flask-boilerplate.svg?branch=master)](https://travis-ci.org/FGtatsuro/flask-boilerplate)

Flask-Boilerplate
=================

Some tasks to create specified projects hierarchy for Flask.

Create specified project hierarchy
----------------------------------

To create boilerplate, you run `task.py` on your project directory.
The example when root module name is `test` is as follows.

```
$ cd <Directory this README exists>
$ pip -r requirements.txt
$ cp task.py <your project directory> && cd <your project directory>
$ python task.py init --root test
running init
running heroku
running hierarchy

# boilerplate
$ ls -R
Procfile    run.py      runtime.txt task.py     test

./test:
__init__.py    controllers.py models.py      static         templates

./test/static:
css

./test/static/css:
style.css

./test/templates:
layout

./test/templates/layout:
layout.html
```

And we can modify names of model/controller modules as follows.
In following case, the name of controller module is `con`, and the one of model module is `mod`.

```
$ python task.py init --root test --controller con --model mod
running init
running heroku
running hierarchy

# boilerplate with custom names of model/controller modules
$ ls -R
Procfile    run.py      runtime.txt task.py     test

./test:
__init__.py con.py      mod.py      static      templates

./test/static:
css

./test/static/css:
style.css

./test/templates:
layout

./test/templates/layout:
layout.html
```

Once the boilerplate is created, `task.py` isn't needed. Thus you can remove it from your project.

```
$ rm task.py
```
