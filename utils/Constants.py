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
    POW            =   '^'

    LPAREN         =   '('
    RPAREN         =   ')'
    LSQUARE        =   '['
    RSQUARE        =   ']'

    DOT            =   '.'
    UNDERSCORE     =   '_'
    COMMA          =   ','
    COLON          =   ':'

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

    FOR         =   'FOR'
    WHILE       =   'WHILE'
    TO          =   'TO'
    STEP        =   'STEP'

    STRING      =   'STRING'

    LSQUARE     =   'LSQUARE'
    RSQUARE     =   'RSQUARE'
    COMMA       =   'COMMA'
    COLON       =   'COLON'

    PRINT       =   'PRINT'
    INPUT       =   'INPUT'

KEYWORDS = [
    'VAR',
    'AND',
    'OR',
    'NOT',
    'IF',
    'THEN',
    'ELIF',
    'ELSE',
    'FOR',
    'TO',
    'STEP',
    'WHILE',
    'PRINT',
    'INPUT'
]

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
