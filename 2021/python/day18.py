import heapq


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_magnitude(self):
        left_magnitude = self.left if isinstance(
            self.left, int) else self.left.get_magnitude()
        right_magnitude = self.right if isinstance(
            self.right, int) else self.right.get_magnitude()
        return 3 * left_magnitude + 2 * right_magnitude


infile = open("inputs/day18.in", "r")
nodes = [eval(line.strip().replace(']', ')').replace('[', 'Node('))
         for line in infile.readlines()]

print(nodes)
print([node.get_magnitude() for node in nodes])


def add_nodes(node1, node2):
    return Node(node1, node2)


def reduce_node(node):
    pass


def explode_node(node):
    pass


def split_node(node):
    pass
