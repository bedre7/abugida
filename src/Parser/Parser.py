from utils.Constants import TOKENS
from src.Parser.Nodes.VarAccessNode import VarAccessNode
from src.Parser.Nodes.VarAssignNode import VarAssignNode
from src.Parser.Nodes.BinOpNode import BinOpNode
from src.Parser.Nodes.NumberNode import NumberNode
from src.Parser.ParseResult import ParseResult
from src.Parser.Nodes.UnaryOpNode import UnaryOpNode
from src.Error.InvalidSyntaxError import InvalidSyntaxError

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
    
    def atom(self):
        response = ParseResult()
        token = self.current_tok

        if token.type in (TOKENS.INT.value, TOKENS.FLOAT.value):
            response.register(self.advance())
            return response.success(NumberNode(token))
        
        elif token.type == TOKENS.IDENTIFIER.value:
            response.register(self.advance())
            return response.success(VarAccessNode(token))

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
            "Expected int, float, '+', '-' or '('"
        ))

    def power(self):
        response = ParseResult()
        left = response.register(self.atom())
        if response.error: return response

        while self.current_tok.type in (TOKENS.POW.value, ):
            operand_token = self.current_tok
            response.register(self.advance())
            right = response.register(self.factor())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)

    def factor(self):
        response = ParseResult()
        token = self.current_tok

        if token.type in (TOKENS.PLUS.value, TOKENS.MINUS.value):
            response.register(self.advance())
            factor = response.register(self.factor())
            
            if response.error: return response
            return response.success(UnaryOpNode(token, factor))

        return self.power()

    def term(self):
        response = ParseResult()
        left = response.register(self.factor())
        if response.error: return response

        while self.current_tok.type in (TOKENS.MUL.value, TOKENS.DIV.value):
            operand_token = self.current_tok
            response.register(self.advance())
            right = response.register(self.factor())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)

    def expression(self):
        response = ParseResult()

        if self.current_tok.matches(TOKENS.KEYWORD.value, 'VAR'):
            response.register(self.advance())

            if self.current_tok.type != TOKENS.IDENTIFIER.value:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected identifier"
                ))
            
            var_name = self.current_tok
            response.register(self.advance())

            if self.current_tok.type != TOKENS.EQUALS.value:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '='"
                ))
            
            response.register(self.advance())
            expr = response.register(self.expression())

            if response.error: return response

            return response.success(
                VarAssignNode(var_name, expr)
            )


        left = response.register(self.term())
        if response.error: return response

        while self.current_tok.type in (TOKENS.PLUS.value, TOKENS.MINUS.value):
            operand_token = self.current_tok
            response.register(self.advance())
            right = response.register(self.term())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)