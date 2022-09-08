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
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RuntimeError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))
        
        return res.success(value)
    
    def visit_VarAssignNode(self, node, context):
        res = RuntimeResult()

        var_name = node.var_name_token.value
        value = res.regiser(self.visit(node.value_node, context))
        if res.error : return res

        context.symbol_table.set(var_name, value)
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

        if error:
            return res.failure(error)

        return res.success(
            number.set_position(node.pos_start, node.pos_end
            ))