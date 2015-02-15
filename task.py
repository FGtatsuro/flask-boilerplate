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
        if (not self.root or not self.controller or not self.model):
            raise Exception("Some options are shortage.")

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
        self.root = None
        self.controller = None
        self.model = None

    def finalize_options(self):
        self.root = self.root or self.__class__._root
        self.controller = self.controller or self.__class__._controller
        self.model = self.model or self.__class__._model
        if (not self.root or not self.controller or not self.model):
            raise Exception("Some options are shortage.")

    def run(self):
        self._create_directory()
        self._create_gitkeep()
        self._create_packages()
        self._create_controller()
        self._create_model()
        self._create_static()
        self._create_template()
        self._create_runscript()

    def _create_directory(self):
        dirs = [os.path.join(self.root, d) for d in
                ('controller', 'model', 'static/css',
                 'templates/layout', 'templates/{0}'.format(self.root))]
        for d in dirs:
            try:
                os.makedirs(d)
            except Exception as e:
                print('    {0}:{1}'.format(d, e.strerror))
        return dirs

    def _create_gitkeep(self):
        dirs = [os.path.join(self.root, d) for d in
                ('controller', 'model', 'static/css',
                 'templates/layout', 'templates/{0}'.format(self.root))]
        for d in dirs:
            f = os.path.join(d, '.gitkeep')
            with open(f, 'w'):
                pass

    def _create_packages(self):
        dirs = [os.path.join(self.root, d) for d in ('controller', 'model')]
        dirs.append(self.root)
        for d in dirs:
            f = os.path.join(d, '__init__.py')
            with open(f, 'w'):
                pass

    def _create_controller(self):
        f = os.path.join(
            self.root, 'controller', '{0}.py'.format(self.controller))
        with open(f, 'w'):
            pass

    def _create_model(self):
        f = os.path.join(
            self.root, 'model', '{0}.py'.format(self.model))
        with open(f, 'w'):
            pass

    def _create_static(self):
        f = os.path.join(self.root, 'static/css', 'style.css')
        with open(f, 'w'):
            pass

    def _create_template(self):
        f = os.path.join(self.root, 'templates/layout/layout.html')
        with open(f, 'w'):
            pass

    def _create_runscript(self):
        f = 'run.py'
        with open(f, 'w'):
            pass

setup(cmdclass={'init': Init, 'heroku': Heroku, 'hierarchy': Hierarchy})
