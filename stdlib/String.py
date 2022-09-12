class String:
    def __init__(self, value):
        self.value = value
    
    def concat(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None