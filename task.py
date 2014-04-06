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
    sub_commands = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        pass

setup(cmdclass={'init': Init})
