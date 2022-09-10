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
    EOF         =   'EOF'

    EQUALS      =   'EQUALS'
    PLUS        =   'PLUS'
    MINUS       =   'MINUS'
    MUL         =   'MUL'
    DIV         =   'DIV'
    POW         =   'POW'
    LPAREN      =   'LPAREN'
    RPAREN      =   'RPAREN'

    EQ          =   'EQ'
    NEQ         =   'NEQ'
    LTH         =   'LTH'
    GTH         =   'GTH'
    LTHE        =   'LTHE'
    GTHE        =   'GTHE'
    AND         =   'AND'
    OR          =   'OR'
    NOT         =   'NOT'

    IF          =   'IF'
    THEN        =   'THEN'
    ELIF        =   'ELIF'
    ELSE        =   'ELSE'

KEYWORDS = [
    'VAR',
    'AND',
    'OR',
    'NOT',
    'IF',
    'THEN',
    'ELIF',
    'ELSE'
]

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
