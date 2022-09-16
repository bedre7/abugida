class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.advance_count = 0
        self.last_registered_count = 0
        self.to_reverse_count = 0
    
    def register_advance(self):
        self.last_registered_count = 1
        self.advance_count += 1
    
    def register(self, response):
        self.last_registered_count = response.advance_count
        self.advance_count += response.advance_count
        if response.error: self.error = response.error
        return response.node

    def try_register(self, response):
        if response.error:
            self.to_reverse_count = response.advance_count
            return None
        
        return self.register(response)

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.advance_count == 0:
            self.error = error
        return self