###########################################
##############       TOKENS     ##########
##########################################

from enum import Enum


class TOKENS(Enum):
    INT      =   'INT'
    FLOAT    =   'FLOAT'
    PLUS     =   'PLUS'
    MINUS    =   'MINUS'
    MUL      =   'MUL'
    DIV      =   'DIV'
    LPAREN   =   'LPAREN'
    RPAREN   =   'RPAREN'
    EOF      =   'EOF'
    POW      =    'POW'

class Token:
    def __init__(self, type_, value = None, pos_start = None, pos_end = None):
        self.type = type_
        self.value = value

        if pos_start: 
            self.pos_start = pos_start.clone()
            self.pos_end = pos_start.clone()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.clone() 

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'