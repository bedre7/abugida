class WhileNode:
    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node

        self.pos_start = condition_node.pos_start
        self.pos_end = body_node.pos_end