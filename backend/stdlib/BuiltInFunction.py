import os
from src.Helpers.SymbolTable import SymbolTable
from src.Interpreter.RuntimeResult import RuntimeResult
from stdlib.Number import Number
from stdlib.String import String
from stdlib.List import List
from utils.Context import Context
from .Type import Type

class BuiltInFunction(Type):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<anonymous>"
    
    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context
    
    def check_args(self, arg_names, args):
        response = RuntimeResult()

        if len(args) > len(arg_names):
            return response.failure(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} - too many arguments passed into {self.name}",
                self.context
            )

        if len(args) < len(arg_names):
            return response.failure(
                self.pos_start, self.pos_end,
                f"{len(arg_names) - len(args)} - too few arguments passed into {self.name}",
                self.context
            )
        
        return response.success(None)
        
    def populate_args(self, arg_names, args, execution_ctx):
        for i in range(len(args)):
            arg_name = arg_names[i]
            arg_value = args[i]
            arg_value.set_context(execution_ctx)
            execution_ctx.symbol_table.set_value(arg_name, arg_value)
    
    def check_and_populate_args(self, arg_names, args, execution_ctx):
        response = RuntimeResult()
        response.register(self.check_args(arg_names, args))
        if response.error: return response
        self.populate_args(arg_names, args, execution_ctx)
        return response.success(None)
    
    def execute(self, args):
        response = RuntimeResult()
        execution_ctx = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        response.register(self.check_and_populate_args(method.arg_names, args, execution_ctx))
        if response.error: return response

        return_value = response.register(method(execution_ctx))
        if response.error: return response

        return response.success(return_value)
    
    def no_visit_method(self):
        raise Exception(f'No execute_{self.name} method defined')
    
    def execute_print(self, execution_ctx):
        print(str(execution_ctx.symbol_table.get("value")))
        return RuntimeResult().success(Number.null)
    execute_print.arg_names = ["value"]

    def execute_input(self, execution_ctx):
        pass
    
    def execute_clear(self, execution_ctx):
        os.system('cls' if os.name == 'nt' else 'clear')
        return RuntimeResult().success(Number.null)
    execute_clear.arg_names = []

    def execute_is_number(self, execution_ctx):
        is_number = isinstance(execution_ctx.symbol_table.get("value"), Number)
        return RuntimeResult().success(Number.true if is_number else Number.false)
    execute_is_number.arg_names = ["value"]

    def execute_is_string(self, execution_ctx):
        is_string = isinstance(execution_ctx.symbol_table.get("value"), String)
        return RuntimeResult().success(Number.true if is_string else Number.false)
    execute_is_number.arg_names = ["value"]

    def execute_is_list(self, execution_ctx):
        is_list = isinstance(execution_ctx.symbol_table.get("value"), List)
        return RuntimeResult().success(Number.true if is_list else Number.false)
    execute_is_number.arg_names = ["value"]


    def clone(self):
        new_func = BuiltInFunction(self.name)
        new_func.set_context(self.context)
        new_func.set_position(self.pos_start, self.pos_end)
        return new_func
    
    def __repr__(self) -> str:
        return f'<Built-in function {self.name}>'

BuiltInFunction.print       = BuiltInFunction("print")
BuiltInFunction.input       = BuiltInFunction("input")
BuiltInFunction.clear       = BuiltInFunction("clear")
BuiltInFunction.is_number   = BuiltInFunction("is_number")
BuiltInFunction.is_string   = BuiltInFunction("is_string")
BuiltInFunction.is_list     = BuiltInFunction("is_list")