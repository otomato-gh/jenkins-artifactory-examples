#!/usr/bin/env python

from setuptools import setup

setup(
    name='otomato-python-example',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='Otomato',
    author_email='contact@otomato.com',
    url='https://github.com/otomato-gh/jenkins-artifactory-examples',
    packages=['pythonExample'],
    install_requires=['PyYAML>3.11', 'nltk'],
)
