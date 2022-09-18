class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
    
    def get_value(self, var_name):
        value = self.symbols.get(var_name, None)

        if value == None and self.parent:
            return self.parent.get_value(var_name)
        
        return value

    def set_value(self, var_name, value):
        self.symbols[var_name] = value
    
    def remove(self, var_name):
        del self.symbols[var_name]