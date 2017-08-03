#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-dsl
------------

Tests for `django-dsl` module.
"""
from distutils.errors import CCompilerError

from django.core.exceptions import ValidationError
from django.test import TestCase

from django_dsl import compiler
from django_dsl.fields import DjangoDSLField
from django_dsl.validators import DjangoDSLValidator
from django_dsl import exceptions

class TestDjango_dsl(TestCase):
    def test_dsl(self):
        shortcuts = {
            "g": "groups__name",
            "s": "state__name"
        }
        input = '(modified >= 2011-1-1 AND NOT s = "OK") OR g="XXX"'
        res = compiler.compile(input, shortcuts)
        assert res.children[1][0] == "groups__name"

    def test_null(self):
        res = compiler.compile("modified = NULL")
        assert res.children[0][1] is None

        res = compiler.compile('modified = "NULL"')
        assert res.children[0][1] == "NULL"

    def test_in(self):
        compiler.compile("modified IN [ 123 ]")
        compiler.compile("modified IN [ 123 , 123 ]")
        compiler.compile("modified = [ 123 , 123 , 123 ]")
        compiler.compile('range IN [1, "2", 2011-1-1]')
        compiler.compile("""range 


IN [1, "2", 2011-1-1]""")

    def test_validation(self):
        self.assertRaises(
            ValidationError,
            DjangoDSLValidator,
            None)

        self.assertRaises(
            ValidationError,
            DjangoDSLValidator,
            "  ")

        self.assertRaises(
            ValidationError,
            DjangoDSLValidator,
            "110g8 ru08q35 0g80as8d u1!! !+!)")

    def test_field(self):
        f = DjangoDSLField()
        assert DjangoDSLValidator in f.validators

    def test_t_error_bug(self):
        with self.assertRaises(exceptions.CompileException):
            compiler.compile("some_field ~ 'test'")