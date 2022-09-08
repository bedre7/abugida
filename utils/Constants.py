from enum import Enum

class SPECIAL_CHARS(Enum):
    WHITESPACE  =   ' \t\n'
    NEWLINE   =   '\n'
    SPACE     =   ' '
    PLUS      =   '+'
    MINUS     =   '-'
    MUL       =   '*'
    DIV       =   '/'
    LPAREN    =   '('
    RPAREN    =   ')'
    DOT       =   '.'
    POW       =   '^'

DIGITS = '0123456789'
