# coding:utf-8
from pathlib import Path

import ply.lex as lex
from ply.yacc import yacc

yacc.yaccdebug = False


def compile(expr, shortcuts=None):
    if shortcuts is None:
        shortcuts = {}

    from . import lexer
    lexer = lex.lex(module=lexer)

    from . import parser as dsl_parser

    # I love David Beazley and he's a great guy, I also like how easy it is
    # to extend PLY, but this could really use some re-work. This is not
    # thread safe at all and we're playing with module globals here.
    dsl_parser.get_shortcut = lambda key: shortcuts[key]

    parser = yacc(
        module=dsl_parser,
        debug=False,
        picklefile=Path(__file__).parent / "parser_pickled.bin"
    )
    return parser.parse(expr, lexer=lexer)
