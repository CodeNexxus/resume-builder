class AST:
    def __init__(self):
        self.root = None
        self.current_number = 0

    def get_pre_order(self):
        self.pre_order(self.root)

    def pre_order(self,node):
        print(node.value)
        for child in node.children:
            self.pre_order(child)

    class TreeNode:
        def __init__(self, value, children, number):
            self.value = value
            self.children = children
            self.number = number


    def make_node(self, value, children):
        tree_node = self.TreeNode(value, children, self.current_number)
        self.current_number += 1
        return tree_node

    def add_child(self, node, new_child):
        if node.children is None:
            node.children = [].append(new_child)
        else:
            node.children.append(new_child)
