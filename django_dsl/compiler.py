# coding:utf-8

import ply.lex as lex
from ply.yacc import yacc

from .exceptions import NoSuchShortcutError

__shotcuts = None


def register_shortcut(key, value):
    __shotcuts[key] = value


def get_shortcut(key):
    try:
        return __shotcuts[key]
    except KeyError:
        raise NoSuchShortcutError(key)


def compile(expr):
    from . import lexer
    lexer = lex.lex(module=lexer)

    from . import parser as dsl_parser
    parser = yacc(module=dsl_parser)

    return parser.parse(expr, lexer=lexer)
