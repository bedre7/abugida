from .Type import Type
from stdlib.Number import Number
from src.Error.RuntimeError import RuntimeError

class List(Type):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements
    
    def add_to(self, other):
        if isinstance(other, Number):
            new_list = self.clone()
            new_list.elements.append(other)
            return new_list, None
        if isinstance(other, List):
            new_list = self.clone()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Type.illegal_operation(self, other)
    
    def subb_by(self, other):
        if isinstance(other, List):
            new_list = self.clone()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RuntimeError(
                    other.pos_start, other.pos_end,
                    "Index out of range", self.context
                )
        else:
            return None, Type.illegal_operation(self, other)

    def clone(self):
        new_list = List(self.elements)
        new_list.set_position(self.pos_start, self.pos_end)
        new_list.set_context(self.context)

        return new_list

    def __repr__(self) -> str:
        return f'[{", ".join([str(x) for x in self.elements])}]'