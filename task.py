#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    user_options = []
    sub_commands = [('heroku', None)]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        [self.run_command(sub) for sub in self.get_sub_commands()]
        print('init')


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
            f.write('python-3.3.2')

setup(cmdclass={'init': Init, 'heroku': Heroku})
