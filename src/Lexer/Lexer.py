from pickle import FALSE
from src.Error.IllegelCharError import IllegelCharError
from src.Error.ExpectedCharError import ExpectedCharError
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
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char == SYMBOLS.MINUS.value:
                tokens.append(self.make_minus_or_arrow())
            elif self.current_char == SYMBOLS.PLUS.value:
                tokens.append(Token(TOKENS.PLUS.value, pos_start=self.position))
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
            elif self.current_char == SYMBOLS.LPAREN.value:
                tokens.append(Token(TOKENS.LPAREN.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.RPAREN.value:
                tokens.append(Token(TOKENS.RPAREN.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SYMBOLS.NEQ.value:
                token, error = self.make_not_equals()
                if error: return [], error
                tokens.append(token)
            elif self.current_char == SYMBOLS.EQUALS.value:
                tokens.append(self.make_equals())
            elif self.current_char == SYMBOLS.LTH.value:
                tokens.append(self.make_less_than())
            elif self.current_char == SYMBOLS.GTH.value:
                tokens.append(self.make_greater_than())
            elif self.current_char == SYMBOLS.COMMA.value:
                tokens.append(Token(TOKENS.COMMA.value, pos_start=self.position))
                self.advance()
            else:
                pos_start = self.position.clone()
                char = self.current_char
                self.advance()
                return [], IllegelCharError(pos_start, self.position, f"Unexpected char '{char}'")

        tokens.append(Token(TOKENS.EOF.value, pos_start = self.position))
        return tokens, None
    
    def make_not_equals(self):
        pos_start = self.position.clone()
        self.advance()

        if self.current_char == SYMBOLS.EQUALS.value:
            self.advance()
            return Token(TOKENS.NEQ.value, pos_start=pos_start, pos_end=self.position), None
        
        self.advance()
        return None, ExpectedCharError(pos_start, self.position
        , "'=' (after '!')")
    
    def make_equals(self):
        token_type = TOKENS.EQUALS.value

        pos_start = self.position.clone()
        self.advance()

        if self.current_char == SYMBOLS.EQUALS.value:
            token_type = TOKENS.EQ.value
            self.advance()
        
        return Token(token_type, pos_start=pos_start, pos_end=self.position)
    
    def make_less_than(self):
        token_type = TOKENS.LTH.value

        pos_start = self.position.clone()
        self.advance()

        if self.current_char == SYMBOLS.EQUALS.value:
            token_type = TOKENS.LTHE.value
            self.advance()
        
        return Token(token_type, pos_start=pos_start, pos_end=self.position)
    
    def make_greater_than(self):
        token_type = TOKENS.GTH.value

        pos_start = self.position.clone()
        self.advance()

        if self.current_char == SYMBOLS.EQUALS.value:
            token_type = TOKENS.GTHE.value
            self.advance()
        
        return Token(token_type, pos_start=pos_start, pos_end=self.position)
    
    def make_identifier(self):
        identifier = ''
        pos_start = self.position.clone()

        while self.current_char != None and self.current_char in LETTERS_DIGITS + SYMBOLS.UNDERSCORE.value:
            identifier += self.current_char
            self.advance()
        
        token_type = TOKENS.KEYWORD.value if identifier in KEYWORDS else TOKENS.IDENTIFIER.value
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
    
    def make_string(self):
        string = ''
        pos_start = self.position.clone()

        escape_char = False
        self.advance()

        escape_chars = {
            'n': '\n',
            't': '\t'
        }

        while self.current_char != None and (self.current_char != '"' or escape_char):
            if escape_char:
                string += escape_chars.get(self.current_char, self.current_char)
            else:
                if self.current_char == '\\':
                    escape_char = True
                else: 
                    string += self.current_char

            self.advance()
            escape_char = False

        self.advance()
        return Token(TOKENS.STRING.value, string, pos_start, self.position)
    
    def make_minus_or_arrow(self):
        token_type = TOKENS.MINUS.value
        pos_start = self.position.clone()
        self.advance()

        if self.current_char == '>':
            self.advance()
            token_type = TOKENS.ARROW.value
        
        return Token(token_type, pos_start=pos_start, pos_end=self.position)


