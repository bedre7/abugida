from src.Lexer.Token import TOKENS
from src.Parser.BinOpNode import BinOpNode
from src.Parser.NumberNode import NumberNode
from src.Parser.ParseResult import ParseResult
from src.Error.InvalidSyntaxError import InvalidSyntaxError
from src.Parser.UnaryOpNode import UnaryOpNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = -1
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_tok = self.tokens[self.token_index]
        return self.current_tok
    
    def parse(self):
        response = self.expression()

        if not response.error and self.current_tok.type != TOKENS.EOF.value:
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end, 
                "Expected '+', '-', '/' or '*'"
            ))

        return response

    def factor(self):
        response = ParseResult()
        token = self.current_tok

        if token.type in (TOKENS.PLUS.value, TOKENS.MINUS.value):
            response.register(self.advance())
            factor = response.register(self.factor())
            
            if response.error: return response
            return response.success(UnaryOpNode(token, factor))

        elif token.type in (TOKENS.INT.value, TOKENS.FLOAT.value):
            response.register(self.advance())
            return response.success(NumberNode(token))
        
        elif token.type == TOKENS.LPAREN.value:
            response.register(self.advance())
            expression = response.register(self.expression())

            if response.error: return response
            if self.current_tok.type == TOKENS.RPAREN.value:
                response.register(self.advance())
                return response.success(expression)
            else:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))

        return response.failure(InvalidSyntaxError(
            token.pos_start, token.pos_end, 
            "Expected int or float"
        ))

    def term(self):
       return self.binary_operation(self.factor, (TOKENS.MUL.value, TOKENS.DIV.value))

    def expression(self):
        return self.binary_operation(self.term, (TOKENS.PLUS.value, TOKENS.MINUS.value))
    
    def binary_operation(self, func, operation_tokens ):
        response = ParseResult()
        left = response.register(func())
        if response.error: return response

        while self.current_tok.type in operation_tokens:
            operand_token = self.current_tok
            response.register(self.advance())
            right = response.register(func())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)