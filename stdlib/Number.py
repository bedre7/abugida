from src.Error.RuntimeError import RuntimeError
class Number:
    def __init__(self, value):
        self.value = value
        self.set_position()
        self.set_context()
    
    def set_position(self, pos_start = None, pos_end = None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def add_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subb_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

    def mult_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def raised_to(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None

    def div_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RuntimeError(
                    other.pos_start, other.pos_end,
                    "Division by zero",
                    self.context
                )

            return Number(self.value / other.value).set_context(self.context), None
    
    def __repr__(self) -> str:
        return str(self.value)