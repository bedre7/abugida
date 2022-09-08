from distutils.log import error


class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
    
    def register(self, response):
        if isinstance(response, ParseResult):
            if response.error: self.error = response.error
            return response.node
        
        # if it's a node
        return response

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self