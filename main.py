from stdlib.Number import Number
from stdlib.BuiltInFunction import BuiltInFunction
from src.Helpers.SymbolTable import SymbolTable
from src.Interpreter.Interpreter import Interpreter
from src.Lexer.Lexer import Lexer
from src.Parser.Parser import Parser
from utils.Context import Context

global_symbol_table = SymbolTable()
global_symbol_table.set_value("NULL", Number.null)
global_symbol_table.set_value("TRUE", Number.true)
global_symbol_table.set_value("FALSE", Number.false)
global_symbol_table.set_value("PRINT", BuiltInFunction.print)
global_symbol_table.set_value("INPUT", BuiltInFunction.input)
global_symbol_table.set_value("CLEAR", BuiltInFunction.clear)
global_symbol_table.set_value("CLS", BuiltInFunction.clear)
global_symbol_table.set_value("IS_NUM", BuiltInFunction.is_number)
global_symbol_table.set_value("IS_STR", BuiltInFunction.is_string)
global_symbol_table.set_value("IS_LIST", BuiltInFunction.is_list)

def run(file_name, text):
    #Generate tokens
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()

    if error: return None, error
    #Generate Abstract Syntax Tree
    parser = Parser(tokens)
    AST = parser.parse()
    if AST.error: return None, AST.error
    #Run Program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(AST.node, context)

    return result.value, result.error