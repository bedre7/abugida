class StringNode:
    def __init__(self, token):
        self.token = token

        self.pos_start = token.pos_start
        self.pos_end = token.pos_end

    
    def __repr__(self) -> str:
        return f'{self.token}'