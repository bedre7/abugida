class RuntimeResult:
    def __init__(self):
        self.value = None
        self.error = None
    
    def register(self, response):
        if response.error:
            self.error = response.error
        return response.value
    
    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self