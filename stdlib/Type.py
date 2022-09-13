from src.Interpreter.RuntimeResult import RuntimeResult


class Type:
    def __init__(self):
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
        return None, self.illegal_operation(other)

    def subb_by(self, other):
        return None, self.illegal_operation(other)

    def mult_by(self, other):
       return None, self.illegal_operation(other)

    def raised_to(self, other):
        return None, self.illegal_operation(other)

    def div_by(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
       return None, self.illegal_operation(other)
            
    def get_comparison_neq(self, other):
        return None, self.illegal_operation(other)
            
    def get_comparison_lth(self, other):
        return None, self.illegal_operation(other)
            
    def get_comparison_gth(self, other):
        return None, self.illegal_operation(other)
              
    def get_comparison_lthe(self, other):
       return None, self.illegal_operation(other)
            
    def get_comparison_gthe(self, other):
        return None, self.illegal_operation(other)
            
    def and_with(self, other):
        return None, self.illegal_operation(other)
            
    def or_with(self, other):
        return None, self.illegal_operation(other)
    
    def notted(self):
        return None, self.illegal_operation()
    
    def is_true(self):
        return None, self.illegal_operation()
    
    def execute(self):
        return RuntimeResult().failure(self.illegal_operation())

    def clone(self):
        raise Exception("No copy method defined")

    def illegal_operation(self, other = None):
        if not other: other = self
        return RuntimeError(
            self.pos_start, other.pos_end,
            "Illegal Operation",
            self.context
        )
