#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import os
import os.path
from shutil import copy2
from subprocess import Popen, PIPE
from tempfile import mkdtemp

@contextmanager
def cd(new):
    old = os.getcwd()
    try:
        os.chdir(new)
        yield
    finally:
        os.chdir(old)

def test_heroku():
    d = mkdtemp()
    copy2('task.py', d)
    with cd(d):
        process = Popen('python task.py heroku'.split())
        process.communicate()
        assert process.returncode == 0

        assert os.path.exists('Procfile')
        assert os.path.exists('runtime.txt')

        # Other files doesn't be generated
        actual = set(os.listdir('.'))
        actual.remove('task.py')
        assert len(actual) == 2

        with open('Procfile') as f:
            assert f.read() == 'web: python run.py'
        with open('runtime.txt') as f:
            assert f.read() == 'python-3.4.2'

def test_hierarchy_default():
    d = mkdtemp()
    copy2('task.py', d)
    with cd(d):
        root = 'flaskdefault'
        process = Popen('python task.py hierarchy --root {0}'.format(root).split())
        process.communicate()
        assert process.returncode == 0

        assert os.path.exists(os.path.join(root, 'static/css/.gitkeep'))
        assert os.path.exists(os.path.join(root, 'templates/.gitkeep'))
        assert os.path.exists(os.path.join(root, '__init__.py'))
        assert os.path.exists(os.path.join(root, 'controllers.py'))
        assert os.path.exists(os.path.join(root, 'models.py'))
        assert os.path.exists(os.path.join(root, 'static/css/style.css'))
        assert os.path.exists(os.path.join(root, 'templates/layout.html'))
        assert os.path.exists(os.path.join(root, 'templates/index.html'))
        assert os.path.exists(os.path.join(root, 'templates/items.html'))
        assert os.path.exists(os.path.join(root, 'templates/utils.html'))
        assert os.path.exists('run.py')

        # Flask files doesn't be generated
        assert not os.path.exists('Procfile')
        assert not os.path.exists('runtime.txt')

        # assert only key parts
        with open(os.path.join(root, '__init__.py')) as f:
            content = f.read()
            assert content.find('app = Flask(__name__)') > -1
            assert content.find('app.debug = True') > -1
            assert content.find("app.config['SECRET_KEY'] = ") > -1
            assert content.find('from .controllers import *'.format(root)) > -1

        with open(os.path.join(root, 'controllers.py')) as f:
            content = f.read()
            assert content.find('from . import app') > -1
            assert content.find('from .models import *') > -1
            assert content.find("@app.route") > -1
            assert content.find("items = Dummy()") > -1, 'Controller uses model.'

        with open(os.path.join(root, 'models.py')) as f:
            content = f.read()
            assert content.find('class Dummy(object):') > -1, 'Model used in controller is defined.'

        with open(os.path.join(root, 'templates/layout.html')) as f:
            content = f.read()
            assert content.find('<!DOCTYPE html>') > -1
            assert content.find("{{ url_for('static', filename='css/style.css') }}") > -1
            assert content.find('{% block title %}') > -1
            assert content.find('{% block content %}') > -1

        with open(os.path.join(root, 'templates/index.html')) as f:
            content = f.read()
            assert content.find('{% extends "layout.html" %}') > -1
            assert content.find('{% block title %}') > -1
            assert content.find('{% block content %}') > -1
            assert content.find('{{ super() }}') > -1

        with open(os.path.join(root, 'templates/utils.html')) as f:
            content = f.read()
            assert content.find('macro list(items)') > -1

        with open('run.py') as f:
            content = f.read()
            assert content.find('from {0} import app'.format(root)) > -1
            assert content.find('app.run') > -1

def test_init_default():
    d = mkdtemp()
    copy2('task.py', d)
    with cd(d):
        root = 'flaskdefault'
        process = Popen('python task.py init --root {0}'.format(root).split())
        process.communicate()
        assert process.returncode == 0

        # init = heroku + hierarchy
        assert os.path.exists(os.path.join(root, 'static/css/.gitkeep'))
        assert os.path.exists(os.path.join(root, 'templates/.gitkeep'))
        assert os.path.exists(os.path.join(root, '__init__.py'))
        assert os.path.exists(os.path.join(root, 'controllers.py'))
        assert os.path.exists(os.path.join(root, 'models.py'))
        assert os.path.exists(os.path.join(root, 'static/css/style.css'))
        assert os.path.exists(os.path.join(root, 'templates/layout.html'))
        assert os.path.exists(os.path.join(root, 'templates/index.html'))
        assert os.path.exists(os.path.join(root, 'templates/items.html'))
        assert os.path.exists(os.path.join(root, 'templates/utils.html'))
        assert os.path.exists('run.py')
        assert os.path.exists('Procfile')
        assert os.path.exists('runtime.txt')
