#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
from distutils.command.build import build as _build
from setuptools.command.install_lib import install_lib as _install_lib
from distutils.cmd import Command

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from django_dsl/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("django_dsl", "__init__.py")


class compile_translations(Command):
    description = 'compile message catalogs to MO files via django compilemessages'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        curdir = os.getcwd()
        os.chdir(os.path.realpath('django_dsl'))
        from django.core.management import call_command
        call_command('compilemessages')
        os.chdir(curdir)


class build(_build):
    sub_commands = [('compile_translations', None)] + _build.sub_commands


class install_lib(_install_lib):
    def run(self):
        self.run_command('compile_translations')
        _install_lib.run(self)


        
if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-dsl',
    version=version,
    description="""DSL for Django ORM""",
    long_description=readme + '\n\n' + history,
    author='Michał Pasternak',
    author_email='michal.dtz@gmail.com',
    url='https://github.com/mpasternak/django-dsl',
    packages=[
        'django_dsl',
    ],
    include_package_data=True,
    install_requires=["ply>=3.10", "Django>=1.10"],
    license="MIT",
    zip_safe=False,
    keywords='django-dsl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass={'build': build, 'install_lib': install_lib,
        'compile_translations': compile_translations}
)
