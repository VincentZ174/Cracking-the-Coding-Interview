class DirectedGraph:

    def __init__(self, matrix):
        self.matrix = matrix

    def is_adj(self, node_one, node_two):
        if self.matrix[node_one][node_two]:
            return True
        else:
            return False


# example taken from the textbook
example_matrix = [[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 0, 0, 0],
                  [0, 0, 1, 0]]

dg = DirectedGraph(example_matrix)

print(dg.is_adj(0, 1))  # Returns True if there exists a path
