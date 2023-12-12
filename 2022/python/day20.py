class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_values():
    with open('inputs/day20.in', 'r') as infile:
        values = [Node(int(l)) for l in infile.read().splitlines()]
        for i in range(len(values) - 1):
            values[i].right = values[i+1]
        for i in range(1, len(values)):
            values[i].left = values[i-1]
        values[0].left = values[-1]
        values[-1].right = values[0]
    return values


def insert_node(me, insert_left):
    left = me.left
    right = me.right
    right.left = left
    left.right = right

    insert_right = insert_left.right
    insert_left.right = me
    insert_right.left = me
    me.right = insert_right
    me.left = insert_left


decryption = [1, 811589153]
iterations = [1, 10]
for d, iter in zip(decryption, iterations):
    values = parse_values()
    length = len(values)
    for _ in range(iter):
        for index, v in enumerate(values):
            if (v.value * d) % (length - 1) == 0:
                continue

            insert_left = v
            for _ in range(v.value * d % (length - 1)):
                insert_left = insert_left.right
            insert_node(v, insert_left)

    head = [v for v in values if v.value == 0][0]
    nums = [head.value]
    curr = head.right
    while curr != head:
        nums.append(curr.value)
        curr = curr.right
    print(nums[1000 % length], nums[2000 % length], nums[3000 % length],
          (nums[1000 % length] + nums[2000 % length] + nums[3000 % length]) * d)
