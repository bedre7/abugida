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
    NEQ            =   '!='
    LTH            =   '<'
    GTH            =   '>'
    LTHE           =   '<='
    GTHE           =   '>='

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
    POW         =   'POW'
    RPAREN      =   'RPAREN'
    EOF         =   'EOF'
    EQ          =   'EQ'
    NEQ         =   'NEQ'
    LTH         =   'LTH'
    GTH         =   'GTH'
    LTHE        =   'LTHE'
    GTHE        =   'GTHE'
    AND         =   'AND'
    OR          =   'OR'
    NOT         =   'NOT'

KEYWORDS = [
    'VAR',
    'AND',
    'OR',
    'NOT'
]

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
