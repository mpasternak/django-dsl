=============================
Django DSL
=============================

.. image:: https://badge.fury.io/py/django-dsl.svg
    :target: https://badge.fury.io/py/django-dsl

.. image:: https://github.com/mpasternak/django-dsl/actions/workflows/tests.yml/badge.svg?branch=master
    :target: https://github.com/mpasternak/django-dsl/actions/workflows/tests.yml

.. warning::

    **This project is not actively maintained.** Consider using
    `djangoql <https://github.com/ivelum/djangoql>`_ instead, which provides
    a more feature-rich query language for Django ORM.

DSL for Django ORM

This is a simple query language for Django ORM. You can give it to your
customers so they will be able to filter the database without having
to edit code.

From one side, you feed it with a string, supplied by the user. And, it
gives you Q-objects, ready to be used in ``QuerySet.filter()`` call.

Please see ``tests/test_dsl.py`` file for example usage.


Supported versions
------------------

+------------+------+------+------+------+
|            | 3.10 | 3.11 | 3.12 | 3.13 |
+============+======+======+======+======+
| Django 4.2 |  Yes |  Yes |  Yes |  Yes |
+------------+------+------+------+------+
| Django 5.1 |  Yes |  Yes |  Yes |  Yes |
+------------+------+------+------+------+
| Django 5.2 |  Yes |  Yes |  Yes |  Yes |
+------------+------+------+------+------+


Running Tests
-------------

Does the code actually work?

::

    uv sync --extra test
    uv run pytest


License
-------

MIT
