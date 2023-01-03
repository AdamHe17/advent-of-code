class Node:
    def __init__(self, left, right, value, depth):
        self.left = left
        self.right = right
        self.value = value
        self.depth = depth

    def get_magnitude(self):
        # left_magnitude = self.left if isinstance(
        #     self.left, int) else self.left.get_magnitude()
        # right_magnitude = self.right if isinstance(
        #     self.right, int) else self.right.get_magnitude()
        # return 3 * left_magnitude + 2 * right_magnitude
        pass


def parse_nodes(snailfish, depth=0):
    if isinstance(snailfish, int):
        node = Node(None, None, snailfish, depth)
        return node, node

    a, b = snailfish
    ahead, atail = parse_nodes(a, depth+1)
    bhead, btail = parse_nodes(b, depth+1)
    atail.right = bhead
    bhead.left = atail
    return ahead, btail

def print_node(head):
    curr = head
    while curr:
        print(f'{curr.value}:{curr.depth}', end=' ')
        curr = curr.right
    print()

with open("inputs/day18.in", "r") as infile:
    lines = map(eval, infile.read().splitlines())
    nodes = []
    for line in lines:
        head, tail = parse_nodes(line)
        # print_node(head)
        nodes.append(head)


def add_nodes(head1, head2):
    curr = head1
    while curr.right:
        curr.depth += 1
        curr = curr.right
    curr.right = head2
    while curr:
        curr.depth += 1
        curr = curr.right
    return head1

def explode_node(node1, node2):
    assert node1.depth == node2.depth
    if node1.left:
        node1.left.value += node1.value
        node1 = node1.left
    else:
        node1.value = 0
        node1.depth -= 1

    if node2.right:
        node2.right.value += node2.value
        node2 = node2.right
    else:
        node2.value = 0
        node2.depth -= 1

    node1.right = node2
    node2.left = node1


def split_node(node):
    a = node.value // 2
    b = node.value - a
    node.value = a
    node.depth += 1
    right_node = Node(node, node.right, b, node.depth)
    node.right = right_node

def reduce_nodes(head):
    curr = head.right
    while curr:
        if curr.depth == curr.left.depth and curr.depth >= 4:
            explode_node(curr.left, curr)
            return True
        curr = curr.right

    curr = head
    while curr:
        if curr.value >= 10:
            split_node(curr)
            return True
        curr = curr.right

    return False

head, _ = parse_nodes([[[[[9,8],1],2],3],4])
print_node(head)
while reduce_nodes(head):
    print_node(head)
    continue
# explode_node(head, head.right)
print_node(head)