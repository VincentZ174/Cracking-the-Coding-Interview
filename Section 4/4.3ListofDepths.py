class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.add(value)

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __iter__(self):
        node = self
        while node:
            yield str(node.value)
            node = node.next


def binary_tree(array):
    if not array:
        return
    mid = (len(array))//2
    node = Node(array[mid])

    node.left = binary_tree(array[:mid])
    node.right = binary_tree(array[mid+1:])

    return node


def depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        depth_left = 1+depth(tree.left)
        depth_right = 1+depth(tree.right)

        if depth_left > depth_right:
            return depth_left
        else:
            return depth_right


def tree_to_ll(tree, lists={}, level=1):
    d = depth(tree)
    if lists.get(level) is None:
        lists[level] = [LinkedList(tree.value)]
    else:
        lists[level][0].add(tree.value)
        if level == d:
            return lists
    if tree.left is not None:
        lists = tree_to_ll(tree.left, lists, level+1)
    if tree.right is not None:
        lists = tree_to_ll(tree.right, lists, level+1)
    return lists


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = binary_tree(arr)
result = tree_to_ll(bst)

level1 = result[1][0]
level2 = result[2][0]
level3 = result[3][0]
level4 = result[4][0]

print("-----Depth 1-----")
print(level1)

print("-----Depth 2-----")
print(level2)

print("-----Depth 3-----")
print(level3)

print("-----Depth 4-----")
print(level4)

