#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-dsl
------------

Tests for `django-dsl` module.
"""

from django.test import TestCase

from django_dsl import compiler


class TestDjango_dsl(TestCase):
    def test_dsl(self):
        compiler.register_shortcut("g", "groups__name")
        compiler.register_shortcut("s", "state__name")
        input = '(modified >= 2011-1-1 AND NOT s = "OK") OR g="XXX"'

    def test_in(self):
        res = compiler.compile("modified IN [ 123 ]")
        res = compiler.compile("modified IN [ 123 , 123 ]")
        res = compiler.compile("modified = [ 123 , 123 , 123 ]")
        res = compiler.compile('range IN [1, "2", 2011-1-1]')
