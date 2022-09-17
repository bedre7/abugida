class RuntimeResult:
    def __init__(self, node_type=None):
        self.value = None
        self.error = None
        self.node_type = node_type
    
    def register(self, response):
        if response.error:
            self.error = response.error
        return response.value
    
    def success(self, value, node_type=None):
        self.value = value
        self.node_type = node_type
        return self

    def failure(self, error):
        self.error = error
        return self