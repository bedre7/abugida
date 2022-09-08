from enum import Enum
import string

class SYMBOLS(Enum):
    WHITESPACE     =   ' \t\n'
    NEWLINE        =   '\n'
    SPACE          =   ' '
    EQUALS         =   '='
    PLUS           =   '+'
    MINUS          =   '-'
    MUL            =   '*'
    DIV            =   '/'
    LPAREN         =   '('
    RPAREN         =   ')'
    DOT            =   '.'
    POW            =   '^'
    UNDERSCORE     =   '_'

class TOKENS(Enum):
    INT         =   'INT'
    FLOAT       =   'FLOAT'
    IDENTIFIER  =   'IDENTIFIER'
    KEYWORD     =   'KEYWORD'
    EQUALS      =   'EQUALS'
    PLUS        =   'PLUS'
    MINUS       =   'MINUS'
    MUL         =   'MUL'
    DIV         =   'DIV'
    LPAREN      =   'LPAREN'
    RPAREN      =   'RPAREN'
    EOF         =   'EOF'
    POW         =   'POW'

KEYWORDS = [
    'VAR'
]

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
