# -*- encoding: utf-8 -*-
# missing: i* (case insensitive), in, startswith, endswith, day&co, isnull
# TODO: range

tokens = (
    'NUMBER',
    'DATE',
    'STRING',
    'FIELD',
    'U_OP',
    'B_OP',
    'EQUAL',
    'LESSER_GREATER',
    'REGEX',
    'IN'
)

literals = '()[],'

compa2lookup = {
    '=': '',
    '~': 'contains',
    '~~': 'regex',
    '>': 'gt',
    '>=': 'gte',
    '<': 'lt',
    '<=': 'lte',
    'IN': 'in'
}

u_ops = ('NOT',)
b_ops = ('AND', 'OR')
