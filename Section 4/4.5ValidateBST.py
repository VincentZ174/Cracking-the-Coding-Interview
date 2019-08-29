class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                else:
                    return self.insert(value, node.left)
            elif value >= node.value:
                if node.right is None:
                    node.right = Node(value)
                else:
                    return self.insert(value, node.right)

    def pre_order(self, node="Empty"):
        if node == "Empty":
            node = self.root
        if node is not None:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
        else:
            return

    def validate_bst(self, node="Empty"):
        if node == "Empty":
            node = self.root
        if node is not None:
            if node.left is not None and node.left.value < node.value:
                self.validate_bst(node.left)
            elif node.right is not None and node.right.value >= node.value:
                self.validate_bst(node.right)
            else:
                return False
            return True


bst = BinaryTree()

bst.insert(6)
bst.insert(6)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(5)

print(bst.validate_bst())