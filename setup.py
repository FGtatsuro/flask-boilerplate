from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='flask-boilerplate',
      version=version,
      description='',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      classifiers=[
      ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Flask PasteScript',
      author='Tatsuro Fujii',
      author_email='fujiistorage@gmail.com',
      url='https://github.com/FGtatsuro/flask-boilerplate',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
