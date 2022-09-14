from src.Parser.Nodes.StringNode import StringNode
from src.Parser.Nodes.ListNode import ListNode
from utils.Constants import TOKENS
from src.Parser.Nodes.ForNode import ForNode
from src.Parser.Nodes.WhileNode import WhileNode
from src.Parser.Nodes.VarAccessNode import VarAccessNode
from src.Parser.Nodes.VarAssignNode import VarAssignNode
from src.Parser.Nodes.IfNode import IfNode
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
            response.register_advance()
            self.advance()
            
            return response.success(NumberNode(token))
        
        elif token.type == TOKENS.STRING.value:
            response.register_advance()
            self.advance()
            return response.success(StringNode(token))

        elif token.type == TOKENS.IDENTIFIER.value:
            response.register_advance()
            self.advance()
            return response.success(VarAccessNode(token))

        elif token.type == TOKENS.LPAREN.value:
            response.register_advance()
            self.advance()
            expression = response.register(self.expression())

            if response.error: return response
            if self.current_tok.type == TOKENS.RPAREN.value:
                response.register_advance()
                self.advance()
                return response.success(expression)
            else:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))
        
        elif token.type == TOKENS.LSQUARE.value:
            list_expr = response.register(self.list_expr())
            
            if response.error:  return response
            return response.success(list_expr)

        elif token.matches(TOKENS.KEYWORD.value, TOKENS.IF.value):
            if_expr = response.register(self.if_expression())

            if response.error : return response
            return response.success(if_expr)
        
        elif token.matches(TOKENS.KEYWORD.value, TOKENS.FOR.value):
            for_expr = response.register(self.for_expression())
            
            if response.error: return response
            return response.success(for_expr)

        elif token.matches(TOKENS.KEYWORD.value, TOKENS.WHILE.value):
            while_expr = response.register(self.while_expression())
            
            if response.error: return response
            return response.success(while_expr)

        return response.failure(InvalidSyntaxError(
            token.pos_start, token.pos_end, 
            "Expected int, float, identifier, '+', '-' or '('"
        ))

    def power(self):
        response = ParseResult()
        left = response.register(self.atom())
        if response.error: return response

        while self.current_tok.type in (TOKENS.POW.value, ):
            operand_token = self.current_tok
            response.register_advance()
            self.advance()
            right = response.register(self.factor())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)

    def factor(self):
        response = ParseResult()
        token = self.current_tok

        if token.type in (TOKENS.PLUS.value, TOKENS.MINUS.value):
            response.register_advance()
            self.advance()
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
            response.register_advance()
            self.advance()
            right = response.register(self.factor())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)
    
    def arith_expression(self):
        response = ParseResult()
        left = response.register(self.term())
        if response.error: return response

        while self.current_tok.type in (TOKENS.PLUS.value, TOKENS.MINUS.value):
            operand_token = self.current_tok
            response.register_advance()
            self.advance()
            right = response.register(self.term())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)

    def comp_expression(self):
        response = ParseResult()

        if self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.NOT.value):
            op_token = self.current_tok
            response.register_advance()
            self.advance()

            node  = response.register(self.comp_expression())
            if response.error: return response
            return response.success(UnaryOpNode(op_token, node)) 
            
        left = response.register(self.arith_expression())
        if response.error: return response
        
        while self.current_tok.type in (TOKENS.EQ.value, TOKENS.NEQ.value, TOKENS.LTH.value, TOKENS.LTHE.value, TOKENS.GTH.value, TOKENS.GTHE.value):
            operand_token = self.current_tok
            response.register_advance()
            self.advance()
            right = response.register(self.arith_expression())

            if response.error : return response.failure(InvalidSyntaxError(
                 self.current_tok.pos_start, self.current_tok.pos_end, 
                "Expected int, float, identifier, '+', '-', 'NOT' or '('"
            ))
            left = BinOpNode(left, operand_token, right)
        
        return response.success(left)
    
    def if_expression(self):
        response = ParseResult()
        cases = []
        else_case = None

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.IF.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'IF'"
            ))
        
        response.register_advance()
        self.advance()

        condition = response.register(self.expression())
        if response.error: return response

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.THEN.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'THEN'"
            ))
        
        response.register_advance()
        self.advance()

        expr = response.register(self.expression())
        if response.error: return response

        cases.append((condition, expr))

        while self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.ELIF.value):
            response.register_advance()
            self.advance()

            condition = response.register(self.expression())
            if response.error: return response

            if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.THEN.value):
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected 'THEN'"
                ))
            
            response.register_advance()
            self.advance()

            expr = response.register(self.expression())
            if response.error: return response

            cases.append((condition, expr))

        if self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.ELSE.value):
            response.register_advance()
            self.advance()

            else_case = response.register(self.expression())
            if response.error: return response

        return response.success(IfNode(cases, else_case))

    def for_expression(self):
        response = ParseResult()
        
        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.FOR.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier"
            ))
        
        response.register_advance()
        self.advance()

        if self.current_tok.type != TOKENS.IDENTIFIER.value:
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier"
            ))
        
        var_name = self.current_tok
        response.register_advance()
        self.advance()

        if self.current_tok.type != TOKENS.EQUALS.value:
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '='"
            ))
        
        response.register_advance()
        self.advance()

        start_value = response.register(self.expression())
        if response.error: return response

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.TO.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'TO'"
            ))
        
        response.register_advance()
        self.advance()

        end_value = response.register(self.expression())
        if response.error:  return response

        if self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.STEP.value):
            response.register_advance()
            self.advance()

            step_value = response.register(self.expression())
            if response.error: return response
        else:
            step_value = None

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.THEN.value):
             return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expeceted 'THEN'"
            ))
        
        response.register_advance()
        self.advance()

        body = response.register(self.expression())

        if response.error: return response

        return response.success(ForNode(var_name, start_value, end_value, step_value, body))

    def while_expression(self):
        response = ParseResult()

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.WHILE.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'WHILE'"
            ))

        response.register_advance()
        self.advance()

        condition = response.register(self.expression())
        if response.error: return response

        if not self.current_tok.matches(TOKENS.KEYWORD.value, TOKENS.THEN.value):
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'THEN'"
            ))
        
        response.register_advance()
        self.advance()

        body = response.register(self.expression())
        if response.error: return response

        return response.success(WhileNode(condition, body))

    def list_expr(self):
        response = ParseResult()
        element_nodes = []
        pos_start = self.current_tok.pos_start.clone()

        if self.current_tok.type != TOKENS.LSQUARE.value:
            return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected '['"
                )) 
        
        response.register_advance()
        self.advance()

        if self.current_tok.type == TOKENS.RSQUARE.value:
            response.register_advance()
            self.advance()
        else:
            element_nodes.append(response.register(self.expression()))
            if response.error:
                return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected ']', 'VAR', 'IF', 'FOR', 'WHILE', 'FUN', int, float, identifier, '+', '-', '(', '[' or 'NOT'"
                ))

            while self.current_tok.type == TOKENS.COMMA.value:
                response.register_advance()
                self.advance()

                element_nodes.append(response.register(self.expression()))
                if response.error: return response

            if self.current_tok.type != TOKENS.RSQUARE.value:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected ',' or ']'"
                ))

            response.register_advance()
            self.advance()

        return response.success(ListNode(
            element_nodes,
            pos_start,
            self.current_tok.pos_end.clone()
        ))

    def expression(self):
        response = ParseResult()

        if self.current_tok.matches(TOKENS.KEYWORD.value, 'VAR'):
            response.register_advance()
            self.advance()

            if self.current_tok.type != TOKENS.IDENTIFIER.value:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected identifier"
                ))
            
            var_name = self.current_tok
            response.register_advance()
            self.advance()

            if self.current_tok.type != TOKENS.EQUALS.value:
                return response.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '='"
                ))
            
            response.register_advance()
            self.advance()
            expr = response.register(self.expression())

            if response.error: return response

            return response.success(
                VarAssignNode(var_name, expr)
            )


        left = response.register(self.comp_expression())
        if response.error: return response

        while (self.current_tok.type, self.current_tok.value) in ((TOKENS.KEYWORD.value, TOKENS.AND.value), (TOKENS.KEYWORD.value, TOKENS.OR.value)):
            operand_token = self.current_tok
            response.register_advance()
            self.advance()
            right = response.register(self.comp_expression())

            if response.error : return response
            left = BinOpNode(left, operand_token, right)
        
        if response.error:
            return response.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected 'VAR', int, float, identifier, '+', '-' or '('"
            ))

        return response.success(left)