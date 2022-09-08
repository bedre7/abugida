from src.Error.IllegelCharError import IllegelCharError
from utils.Position import Position
from src.Lexer.Token import TOKENS, Token
from utils.Constants import SPECIAL_CHARS, DIGITS

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
                tokens.append(self.classify_number())
            elif self.current_char == SPECIAL_CHARS.PLUS.value:
                tokens.append(Token(TOKENS.PLUS.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SPECIAL_CHARS.MINUS.value:
                tokens.append(Token(TOKENS.MINUS.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SPECIAL_CHARS.MUL.value:
                tokens.append(Token(TOKENS.MUL.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SPECIAL_CHARS.DIV.value:
                tokens.append(Token(TOKENS.DIV.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SPECIAL_CHARS.LPAREN.value:
                tokens.append(Token(TOKENS.LPAREN.value, pos_start=self.position))
                self.advance()
            elif self.current_char == SPECIAL_CHARS.RPAREN.value:
                tokens.append(Token(TOKENS.RPAREN.value, pos_start=self.position))
                self.advance()
            else:
                pos_start = self.position.clone()
                char = self.current_char
                self.advance()
                return [], IllegelCharError(pos_start, self.position, f"Unexpected char '{char}'")

        tokens.append(Token(TOKENS.EOF.value, pos_start = self.position))
        return tokens, None

    def classify_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.position.clone()

        while self.current_char != None and self.current_char in DIGITS + SPECIAL_CHARS.DOT.value:
            if self.current_char == SPECIAL_CHARS.DOT.value:
                if dot_count == 1: break
                dot_count += 1
            
            num_str += self.current_char
            self.advance()
            
        if dot_count == 0:
            return Token(TOKENS.INT.value, int(num_str), pos_start, self.position)
        return Token(TOKENS.FLOAT.value, float(num_str), pos_start, self.position)