from src.Error.RuntimeError import RuntimeError
from src.stdlib.Type import Type

class Number(Type):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def clone(self):
        clone = Number(self.value)
        clone.set_position(self.pos_start, self.pos_end)
        clone.set_context(self.context)
        return clone

    def add_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subb_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

    def mult_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def mod_by(self, other):
        if isinstance(other, Number):
            return Number(self.value % other.value).set_context(self.context), None

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

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None
            
    def get_comparison_neq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None
            
    def get_comparison_lth(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None
            
    def get_comparison_gth(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None
            
    def get_comparison_lthe(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None
            
    def get_comparison_gthe(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(self.context), None
            
    def and_with(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
            
    def or_with(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
    
    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None
    
    def is_true(self):
        return self.value != 0

    def __repr__(self) -> str:
        return str(self.value)

Number.null = Number(0)
Number.true = Number(1)
Number.false = Number(0)
