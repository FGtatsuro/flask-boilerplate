#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paste.script.templates import NoDefault, Template, var
from jinja2 import Template as Jinja2Template


class Boilerplate(Template):
    _template_dir = 'templates'
    summary = 'A boilerplate for Flask project'
    required_templates = []
    vars = [
        var('app_name', 'Flask application name', default=NoDefault),
        var('description', 'One-line description of the package'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
    ]
    @staticmethod
    def template_renderer(body, context, filename=None):
        # If you want to use Template in Paste, please use paste.util.template.paste_script_template_renderer
        return Jinja2Template(body).render(context)

    def check_vars(self, user_vars, command):
        return Template.check_vars(self, user_vars, command)
