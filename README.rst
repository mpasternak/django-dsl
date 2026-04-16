=============================
Django DSL
=============================

.. image:: https://badge.fury.io/py/django-dsl.svg
	   :target: https://badge.fury.io/py/django-dsl

.. image:: https://github.com/mpasternak/django-dsl/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/mpasternak/django-dsl/actions

DSL for Django ORM

This is a simple query language for Django ORM. You can give it to your
customers so they will be able to filter the database without having
to edit code.

From one side, you feed it with a string, supplied by the user. And, it
gives you Q-objects, ready to be used in ``QuerySet.filter()`` call.

Please see ``tests/test_dsl.py`` file for example usage.


Running Tests
-------------

Does the code actually work?

::

    uv sync --extra test
    uv run pytest


License
-------

MIT
