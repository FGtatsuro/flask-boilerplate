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


def test_init_default():
    d = mkdtemp()
    with cd(d):
        project_name = 'test_project'
        app_name = 'test_app'
        process = Popen('paster create --no-interactive -t flask_boilerplate {0} app_name={1}'.format(project_name, app_name).split())
        process.communicate()
        assert process.returncode == 0

        with cd(project_name):
            assert os.path.exists(os.path.join(app_name, '__init__.py'))
            assert os.path.exists(os.path.join(app_name, 'views.py'))
            assert os.path.exists(os.path.join(app_name, 'models.py'))
            assert os.path.exists(os.path.join(app_name, 'static/css/style.css'))
            assert os.path.exists(os.path.join(app_name, 'templates/layout.html'))
            assert os.path.exists(os.path.join(app_name, 'templates/index.html'))
            assert os.path.exists(os.path.join(app_name, 'templates/items.html'))
            assert os.path.exists(os.path.join(app_name, 'templates/utils.html'))
            assert os.path.exists('run.py')
            assert os.path.exists('Procfile')
            assert os.path.exists('runtime.txt')
