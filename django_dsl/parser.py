# -*- encoding: utf-8 -*-


# =============================
#           PARSER
# =============================

from django.db.models import Q

from .dsl import compa2lookup, tokens
from .exceptions import CompileException, NoSuchShortcutError

tokens  # NOQA


def p_expression_b_op(p):
    '''expression : expression B_OP expression'''
    if p[2] == 'AND':
        p[0] = p[1] & p[3]
    elif p[2] == 'OR':
        p[0] = p[1] | p[3]


def p_expression_u_op(p):
    '''expression : U_OP expression'''
    if p[1] == 'NOT':
        p[0] = ~ p[2]


def p_expression_paren(p):
    "expression : '(' expression ')' "
    p[0] = p[2]


def p_operation(p):
    """operation : EQUAL
                 | LESSER_GREATER
                 | REGEX
                 | IN
    """
    p[0] = p[1]


def p_paren_list(val):
    """paren_list : '[' flat_list ']'"""
    val[0] = val[2]


def p_flat_list(val):
    """flat_list : value
                 | value ',' flat_list"""

    val[0] = [val[1]]
    if len(val) > 2:
        val[0].extend(val[3])


def p_expression_ID(p):
    """expression : FIELD operation value
    """
    lookup = compa2lookup[p[2]]

    try:
        from .compiler import get_shortcut
        field = get_shortcut(p[1])
    except NoSuchShortcutError:
        field = p[1]

    if lookup:
        field = '%s__%s' % (field, lookup)

    # In some situations (which ones?), python
    # refuses unicode strings as dict keys for
    # Q(**d)
    field = str(field)

    d = {field: p[3]}

    p[0] = Q(**d)


def p_value(p):
    '''value : STRING
            | NUMBER
            | DATE
            | paren_list
            '''
    p[0] = p[1]


def p_error(p):
    if p:
        raise CompileException(u"Parsing error around token: %s" % p.value)
    raise CompileException(u"Parsing error: unexpected end of expression")


precedence = (
    ('left', 'B_OP'),
    ('right', 'U_OP'),
)
