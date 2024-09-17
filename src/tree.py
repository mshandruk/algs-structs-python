from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value) -> None:
        sub_tree = BinaryTree(value)
        if self.left_child is None:
            self.left_child = sub_tree
        else:
            sub_tree.left_child = self.left_child
            self.left_child = sub_tree

    def insert_right(self, value) -> None:
        sub_tree = BinaryTree(value)
        if self.right_child is None:
            self.right_child = sub_tree
        else:
            sub_tree.right_child = self.right_child
            self.right_child = sub_tree

    def breadth_first_search(self, value) -> bool:
        queue_nodes: deque["BinaryTree"] = deque()
        queue_nodes.append(self)
        while queue_nodes:
            node = queue_nodes.popleft()
            if node.key == value:
                return True

            if node.left_child:
                queue_nodes.append(node.left_child)

            if node.right_child:
                queue_nodes.append(node.right_child)
        return False
