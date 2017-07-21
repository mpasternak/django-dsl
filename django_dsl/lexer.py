# -*- encoding: utf-8 -*-

from datetime import date

from .dsl import tokens, literals, u_ops, b_ops  # NOQA
from .exceptions import CompileException

tokens  # NOQA
literals  # NOQA


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_DATE(t):
    r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})'
    day = int(t.lexer.lexmatch.group('day'))
    month = int(t.lexer.lexmatch.group('month'))
    year = int(t.lexer.lexmatch.group('year'))
    t.value = date(year, month, day)
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_EQUAL = '='

t_LESSER_GREATER = '[<>]=?'

t_REGEX = '~~?'


def t_IN(t):
    r" IN "
    return t


def t_FIELD(t):
    r'[A-Za-z_][\w_]*'
    if t.value in u_ops:
        t.type = 'U_OP'
    elif t.value in b_ops:
        t.type = 'B_OP'
    return t


def t_error(t):
    raise CompileException(u"Cannot make sense of char: %s" % t.value[0])


# ignore tabs and spaces
t_ignore = ' \t'
