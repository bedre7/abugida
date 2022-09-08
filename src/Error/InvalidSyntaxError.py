from src.Error.Error import Error

class InvalidSyntaxError(Error):
    ERROR_NAME = 'Invalid Syntax'
    def __init__(self, pos_start, pos_end, details = ''):
        super().__init__(pos_start, pos_end, self.ERROR_NAME, details)
