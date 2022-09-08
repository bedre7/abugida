from inspect import trace
from utils.string_with_arrows import string_with_arrows
from src.Error.Error import Error

class RuntimeError(Error):
    ERROR_NAME = 'Runtime Error'
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, self.ERROR_NAME, details)
        self.context = context
    
    def message(self) -> str:
        error_line = self.generate_traceback()
        error_line += f'{self.error_name}: {self.details}'
        error_line += '\n\n' + string_with_arrows(self.pos_start.file_text, self.pos_start, self.pos_end)
        
        return error_line

    def generate_traceback(self):
        traceback = ''
        ctx_position = self.pos_start
        ctx = self.context

        while ctx:
            trace_back = f' File {ctx_position.file_name}, line {str(ctx_position.line_num + 1)}, in {ctx.display_name}\n' + trace_back
            ctx_position = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (most recent call - last):\n' + trace_back
