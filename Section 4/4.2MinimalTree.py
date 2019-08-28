class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def minimal_tree(array):
    if not array:
        return
    mid = (len(array))//2
    node = Node(array[mid])

    node.left = minimal_tree(array[:mid])
    node.right = minimal_tree(array[mid+1:])

    return node


def pre_order(tree):
    if tree is not None:
        print(tree.value)
        pre_order(tree.left)
        pre_order(tree.right)
    else:
        return


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = minimal_tree(arr)
pre_order(bst)