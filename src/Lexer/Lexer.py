from src.Error.IllegelCharError import IllegelCharError
from utils.Position import Position
from src.Lexer.Token import *
from utils.Constants import *

class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.position = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.position.advance(self.current_char)
        self.current_char = self.text[self.position.index] if self.position.index < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == SYMBOLS.PLUS.value:
                tokens.append(Token(TOKENS.PLUS.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.MINUS.value:
                tokens.append(Token(TOKENS.MINUS.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.MUL.value:
                tokens.append(Token(TOKENS.MUL.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.DIV.value:
                tokens.append(Token(TOKENS.DIV.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.POW.value:
                tokens.append(Token(TOKENS.POW.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.EQUALS.value:
                tokens.append(Token(TOKENS.EQUALS.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.LPAREN.value:
                tokens.append(Token(TOKENS.LPAREN.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.RPAREN.value:
                tokens.append(Token(TOKENS.RPAREN.value, pos_start=self.position))
                self.advance()
            else:
                pos_start = self.position.clone()
                char = self.current_char
                self.advance()
                return [], IllegelCharError(pos_start, self.position, f"Unexpected char '{char}'")

        tokens.append(Token(TOKENS.EOF.value, pos_start = self.position))
        return tokens, None
    
    def make_identifier(self):
        identifier = ''
        pos_start = self.position.clone()

        while self.current_char != None and self.current_char in LETTERS_DIGITS + SYMBOLS.UNDERSCORE.value:
            identifier += self.current_char
            self.advance()
        
        token_type = TOKENS.KEYWORD.value if identifier in TOKENS.KEYWORD.value else TOKENS.IDENTIFIER.value
        return Token(token_type, identifier, pos_start, self.position)  

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.position.clone()

        while self.current_char != None and self.current_char in DIGITS + SYMBOLS.DOT.value:
            if self.current_char == SYMBOLS.DOT.value:
                if dot_count == 1: break
                dot_count += 1
            
            num_str += self.current_char
            self.advance()
        
        # if numbers like .52 was generated, it's converted to -> 0.52
        if num_str.startswith(SYMBOLS.DOT.value):
            num_str = '0' + num_str
        
        # if numbers like 2. was generated, it's converted to -> 2.0
        if num_str.endswith(SYMBOLS.DOT.value):
            num_str += '0'
            
        if dot_count == 0:
            return Token(TOKENS.INT.value, int(num_str), pos_start, self.position)
       
        return Token(TOKENS.FLOAT.value, float(num_str), pos_start, self.position)