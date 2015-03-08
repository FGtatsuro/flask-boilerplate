#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

from setuptools import Command, setup
from six import add_metaclass


class LowerNameType(type):

    def __new__(cls, cls_name, cls_bases, cls_dict):
        cls = super().__new__(cls, cls_name.lower(), cls_bases, cls_dict)
        return cls


@add_metaclass(LowerNameType)
class CustomCommand(Command):
    pass


class Init(CustomCommand):
    description = "Create skelton project for Flask"
    user_options = [
        ('root=', None, 'root module name'),
        ('controller=', None, 'controller module name'),
        ('model=', None, 'model module name')]
    sub_commands = [('heroku', None), ('hierarchy', None)]

    def initialize_options(self):
        self.root = None
        self.controller = None
        self.model = None

    def finalize_options(self):
        pass

    def run(self):
        # TODO: better way to pass option args to sub commands.
        Hierarchy._root = self.root
        Hierarchy._controller = self.controller
        Hierarchy._model = self.model
        [self.run_command(sub) for sub in self.get_sub_commands()]


class Heroku(CustomCommand):
    description = "Create setting files related to Heroku."
    user_options = []
    sub_commands = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        with open('Procfile', 'w') as f:
            f.write('web: python run.py')
        with open('runtime.txt', 'w') as f:
            f.write('python-3.4.2')


# TODO: Refactor duplicated code
class Hierarchy(CustomCommand):
    description = "Create specified project hierarchy for Flask."
    user_options = [
        ('root=', None, 'root module name'),
        ('controller=', None, 'controller module name'),
        ('model=', None, 'model module name')]
    sub_commands = []

    def initialize_options(self):
        # Default values
        self.root = None
        self.controller = 'controllers'
        self.model = 'models'

    def finalize_options(self):
        # Values passed from parent command precede
        self.root = self.__class__._root or self.root
        self.controller = self.__class__._controller or self.controller
        self.model = self.__class__._model or self.model
        if (not self.root or not self.controller or not self.model):
            raise Exception("Some options are shortage.")

    def run(self):
        self._create_directory()
        self._create_gitkeep()
        self._create_root()
        self._create_controller()
        self._create_model()
        self._create_static()
        self._create_template()
        self._create_runscript()

    def _create_directory(self):
        dirs = [os.path.join(self.root, d) for d in ('static/css', 'templates')]
        for d in dirs:
            try:
                os.makedirs(d)
            except Exception as e:
                print('{0}:{1}'.format(d, e.strerror))
        return dirs

    def _create_gitkeep(self):
        dirs = [os.path.join(self.root, d) for d in ('static/css', 'templates')]
        for d in dirs:
            f = os.path.join(d, '.gitkeep')
            with open(f, 'w'):
                pass

    def _create_root(self):
        init_file = os.path.join(self.root, '__init__.py')
        self._create_module_with_shebang(init_file)
        with open(init_file, 'a') as f:
            f.write("""\
import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

if app.debug:
    app.config['SECRET_KEY'] = 'debug_secretkey'
else:
    app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
DebugToolbarExtension(app)

from .{0} import *
""".format(self.controller))

    def _create_controller(self):
        controller_file = os.path.join(self.root, '{0}.py'.format(self.controller))
        self._create_module_with_shebang(controller_file)
        with open(controller_file, 'a') as f:
            f.write("""\
from flask import render_template, redirect, url_for

from . import app
from .models import *

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/items')
def items():
    items = Dummy()
    return render_template('items.html', items=items)
""")

    def _create_model(self):
        model_file = os.path.join(self.root, '{0}.py'.format(self.model))
        self._create_module_with_shebang(model_file)
        with open(model_file, 'a') as f:
            f.write("""\
class Dummy(object):

    def list(self):
        return [{'title': 'title1'}, {'title': 'title2'}]
""")

    def _create_static(self):
        f = os.path.join(self.root, 'static/css', 'style.css')
        with open(f, 'w'):
            pass

    def _create_template(self):
        template_base = os.path.join(self.root, 'templates/layout.html')
        with open(template_base, 'w') as f:
            f.write("""\
<!DOCTYPE html>
<html>
  <head>
    {% block head %}
      <meta charset="utf-8">
      <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" type="text/css" />
      <title>{% block title %}{% endblock %}</title>
    {% endblock %}
  </head>
  <body>
  <div id="content">{% block content %}{% endblock %}</dib>
  </body>
</html>
""")

        index_template = os.path.join(self.root, 'templates/index.html')
        with open(index_template, 'w') as f:
            f.write("""\
{% extends "layout.html" %}
{% block title %}Hello flask-boilerplate{% endblock %}
{% block head %}
  {{ super() }}
{% endblock %}
{% block content %}
  <h1>Index</h1>
  This is the index page.
{% endblock %}
""")

        items_template = os.path.join(self.root, 'templates/items.html')
        with open(items_template, 'w') as f:
            f.write("""\
{% extends "layout.html" %}
{% block title %}Item Page{% endblock %}
{% block head %}
  {{ super() }}
{% endblock %}
{% block content %}
  <h1>Items</h1>
  {% import "utils.html" as utils %}
  {{ utils.list(items.list()) }}
{% endblock %}
""")

        list_template = os.path.join(self.root, 'templates/utils.html')
        with open(list_template, 'w') as f:
            f.write("""\
{%- macro list(items) %}
  {%- for item in items %}
    <div class="title">{{ item['title'] }}</div>
  {%- endfor %}
{%- endmacro %}
""")

    def _create_runscript(self):
        self._create_module_with_shebang('run.py')
        with open('run.py', 'a') as f:
            f.write("""\
import os
from {0} import app

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=int(os.environ.get('FLASK_PORT', 5000)))
""".format(self.root))

    def _create_module_with_shebang(self, filename):
        with open(filename, 'w') as f:
            f.write('''\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

''')

setup(cmdclass={'init': Init, 'heroku': Heroku, 'hierarchy': Hierarchy})
