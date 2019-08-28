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

    @staticmethod
    def depth(tree):
        if tree is None:
            return 0
        if tree.left is None and tree.right is None:
            return 1
        else:
            depth_left = 1 + BinaryTree.depth(tree.left)
            depth_right = 1 + BinaryTree.depth(tree.right)

            if depth_left > depth_right:
                return depth_left
            else:
                return depth_right

    def check_balance(self, node="Empty"):
        if node == "Empty":
            node = self.root
        if node is not None and node.left is not None and node.right is not None:
            print(node.left)
            print(node.right)
            bal_factor = self.depth(node.left) - self.depth(node.right)
            if bal_factor > abs(1):
                return False
            self.check_balance(node.left)
            self.check_balance(node.right)
            return True
        else:
            return


bst = BinaryTree()

bst.insert(6)
bst.insert(6)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(5)

bst.pre_order()

print(bst.check_balance())
