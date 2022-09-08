from utils.Constants import SYMBOLS

class Position:
    def __init__(self, index, line_num, column_num, file_name, file_text):
        self.index = index
        self.line_num = line_num
        self.column_num = column_num
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_char = None):
        self.index += 1
        self.column_num += 1

        if current_char == SYMBOLS.NEWLINE.value:
            self.goto_next_line()
        
        return self

    def goto_next_line(self):
        self.line_num += 1
        self.column_num = 0

    def clone(self):
        return Position(self.index, self.line_num, self.column_num, self.file_name, self.file_text)
