import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        status = tox.cmdline(self.test_args)
        sys.exit(status)

version = '0.1'

setup(name='Flask-Boilerplate',
      version=version,
      description='Paste template for Flask project.',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      classifiers=[
          'Environment :: Console',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Topic :: Software Development :: Code Generators',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='Flask PasteScript',
      author='Tatsuro Fujii',
      author_email='fujiistorage@gmail.com',
      url='https://github.com/FGtatsuro/flask-boilerplate',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript'
      ],
      tests_require=[
          'tox',
          'PasteScript'
      ],
      dependency_links=[
          'hg+ssh://hg@bitbucket.org/FGtatsuro/pastescript@python3_support#egg=PasteScript'
      ],
      cmdclass={'test': Tox},
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      flask_boilerplate=flask_boilerplate.templates:Boilerplate
      """,
      )
