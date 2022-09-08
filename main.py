from stdlib.Number import Number
from src.Helpers.SymbolTable import SymbolTable
from src.Interpreter.Interpreter import Interpreter
from src.Lexer.Lexer import Lexer
from src.Parser.Parser import Parser
from utils.Context import Context

global_symbol_table = SymbolTable()
global_symbol_table.set_value("null", Number(0))
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