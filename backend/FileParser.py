from src.Parser.Nodes.VarAssignNode import VarAssignNode
import main
from utils.Constants import SYMBOLS

class FileParser:
    def __init__(self, file_name=None):
        self.file_name = file_name
    
    def should_print(self, current_node):
        return not isinstance(current_node, VarAssignNode)

    def execute_run(self):
        script = ''

        try:
            with open(self.file_name, "r") as file:
                script = file.read()
                if script.strip() == '':
                    return

        except Exception as e:
            print(e)
        
        print('>>> አቡጊዳ')
        for line in script.split(SYMBOLS.NEWLINE.value):
            if line.strip() == '':
                continue
            last_visited_node, result, error = main.run(self.file_name, f'{line}\n')

            if error: 
                print(error.message())
            elif self.should_print(last_visited_node):
                print(result.value)
    
    def run_from_script(self, script):
        outputs = []
        errors = []

        for line in script.split(SYMBOLS.NEWLINE.value):
            if line.strip() == '':
                continue

            last_visited_node, result, error = main.run(self.file_name, f'{line}\n')

            if error:
                errors.append(error.message())
            elif self.should_print(last_visited_node):
                outputs.append(str(result.value))
        
        return outputs, errors