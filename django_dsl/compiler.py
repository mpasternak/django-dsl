# coding:utf-8

import ply.lex as lex
from ply.yacc import yacc

from .exceptions import NoSuchShortcutError

__shortcuts = None


def register_shortcut(key, value):
    global __shortcuts
    if __shortcuts is None:
        __shortcuts = {}

    __shortcuts[key] = value


def get_shortcut(key):
    global __shortcuts
    if __shortcuts is None:
        __shortcuts = {}
    try:
        return __shortcuts[key]
    except KeyError:
        raise NoSuchShortcutError(key)


def compile(expr):
    from . import lexer
    lexer = lex.lex(module=lexer)

    from . import parser as dsl_parser
    parser = yacc(module=dsl_parser)

    return parser.parse(expr, lexer=lexer)
