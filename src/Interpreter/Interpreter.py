from stdlib.String import String
from stdlib.Number import Number
from stdlib.List import List
from utils.Constants import TOKENS
from src.Interpreter.RuntimeResult import RuntimeResult
from src.Error.RuntimeError import RuntimeError

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

    def visit_IfNode(self, node, context):
        response = RuntimeResult()

        for condition, expr in node.cases:
            condition_value = response.register(self.visit(condition, context))
            if response.error: return response

            if condition_value.is_true():
                expr_value = response.register(self.visit(expr, context))
                if response.error: return response

                return response.success(expr_value)
        
        if node.else_case:
            else_value = response.register(self.visit(node.else_case, context))
            if response.error: return response
            return response.success(else_value)
        
        return response.success(None)
    
    def visit_ForNode(self, node, context):
        response = RuntimeResult()
        elements = []

        start_value = response.register(self.visit(node.start_value_node, context))
        if response.error: return response

        end_value = response.register(self.visit(node.end_value_node, context))
        if response.error: return response

        if node.step_value_node:
            step_value = response.register(self.visit(node.start_value_node, context))
            if response.error: return response
        else:
            step_value = Number(1)
        
        i = start_value.value

        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value
        
        while condition():
            context.symbol_table.set_value(node.var_name_token.value, Number(i))
            i += step_value.value

            elements.append(response.register(self.visit(node.body_node, context)))
            if response.error: return response

        return response.success(
            List(elements).set_context(context).set_position(node.pos_start, node.pos_end)
        )
    
    def visit_WhileNode(self, node, context):
        response = RuntimeResult()
        elements = []

        while True:
            condition = response.register(self.visit(node.condition_node, context))
            if response.error: return response

            if not condition.is_true(): break

            elements.append(response.register(self.visit(node.body_node, context)))
            if response.error: return response
        
        return response.success(
            List(elements).set_context(context).set_position(node.pos_start, node.pos_end)
        )

    def visit_StringNode(self, node, context):
        return RuntimeResult().success(
            String(node.token.value).set_context(context).set_position(node.pos_start, node.pos_end
            ))
    
    def visit_ListNode(self, node, context):
        response = RuntimeResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(response.register(self.visit(element_node, context)))
            if response.error: return response
        
        return response.success(
            List(elements).set_context(context).set_position(node.pos_start, node.pos_end)
        )
                
        
            