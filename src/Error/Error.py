from utils.string_with_arrows import string_with_arrows

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def message(self) -> str:
        error_line = f'{self.error_name}: {self.details}'
        error_line += f'File {self.pos_start.file_name}, line {self.pos_start.line_num + 1}'
        error_line += '\n\n' + string_with_arrows(self.pos_start.file_text, self.pos_start, self.pos_end)
        
        return error_line