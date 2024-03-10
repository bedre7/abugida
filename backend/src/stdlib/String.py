from src.stdlib.Type import Type
from src.stdlib.Number import Number

class String(Type):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def add_to(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, Type.illegal_operation(self, other)

    def mult_by(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, Type.illegal_operation(self, other)
    
    def is_true(self):
        return len(self.value) > 0
    
    def clone(self):
        new = String(self.value)
        new.set_position(self.pos_start, self.pos_end)
        new.set_context(self.context)
        return new
    
    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f'"{self.value}"'