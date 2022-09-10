from stdlib.Number import Number
from utils.Constants import TOKENS
from src.Interpreter.RuntimeResult import RuntimeResult

class Interpreter:
    def visit(self, node, context):
        # "visit_BinaryOpNode"
        # "visit_NumberNode"
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)
    
    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    def visit_NumberNode(self, node, context):
        return RuntimeResult().success(
            Number(node.token.value).set_context(context).set_position(node.pos_start, node.pos_end)
        )
    
    def visit_VarAccessNode(self, node, context):
        res = RuntimeResult()

        var_name = node.var_name_token.value
        value = context.symbol_table.get_value(var_name)

        if not value:
            return res.failure(RuntimeError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))
        value = value.clone().set_position(node.pos_start, node.pos_end)
        return res.success(value)
    
    def visit_VarAssignNode(self, node, context):
        res = RuntimeResult()

        var_name = node.var_name_token.value
        value = res.register(self.visit(node.value_node, context))
        if res.error : return res

        context.symbol_table.set_value(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context):
        res = RuntimeResult()
        
        left = res.register(self.visit(node.left_node, context))
        if res.error: return res
        
        right = res.register(self.visit(node.right_node, context))
        if res.error: return res

        if node.op_token.type == TOKENS.PLUS.value:
            result, error = left.add_to(right)
        elif node.op_token.type == TOKENS.MINUS.value:
            result, error = left.subb_by(right) 
        elif node.op_token.type == TOKENS.MUL.value:
            result, error = left.mult_by(right) 
        elif node.op_token.type == TOKENS.DIV.value:
            result, error = left.div_by(right)
        elif node.op_token.type == TOKENS.POW.value:
            result, error = left.raised_to(right)
        elif node.op_token.type == TOKENS.EQ.value:
            result, error = left.get_comparison_eq(right)
        elif node.op_token.type == TOKENS.NEQ.value:
            result, error = left.get_comparison_neq(right)
        elif node.op_token.type == TOKENS.LTH.value:
            result, error = left.get_comparison_lth(right)
        elif node.op_token.type == TOKENS.GTH.value:
            result, error = left.get_comparison_gth(right)
        elif node.op_token.type == TOKENS.LTHE.value:
            result, error = left.get_comparison_lthe(right)
        elif node.op_token.type == TOKENS.GTHE.value:
            result, error = left.get_comparison_gthe(right)
        elif node.op_token.matches(TOKENS.KEYWORD.value, TOKENS.AND.value):
            result, error = left.and_with(right)
        elif node.op_token.matches(TOKENS.KEYWORD.value, TOKENS.OR.value):
            result, error = left.or_with(right)

        if error:
            return res.failure(error)

        return res.success(
            result.set_position(node.pos_start, node.pos_end
            ))

    def visit_UnaryOpNode(self, node, context):
        res = RuntimeResult()

        number = res.register(self.visit(node.node, context))
        if res.error: return res

        error = None

        if node.op_token.type == TOKENS.MINUS.value:
            number, error = number.mult_by(Number(-1))
        elif node.op_token.matches(TOKENS.KEYWORD.value, TOKENS.AND.value):
            number, error = number.notted()

        if error:
            return res.failure(error)

        return res.success(
            number.set_position(node.pos_start, node.pos_end
            ))