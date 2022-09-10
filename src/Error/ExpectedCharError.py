from src.Error.Error import Error

class ExpectedCharError(Error):
    ERROR_NAME = 'Expected Character'
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, self.ERROR_NAME, details)