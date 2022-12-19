with open('inputs/day8.in', 'r') as infile:
    lines = infile.readlines()
    trees = []
    for line in lines:
        trees.append([int(i) for i in line.strip()])

visible = set()
size = len(trees)
for i in range(size):
    start = -1
    for j in range(size):
        if trees[i][j] > start:
            start = trees[i][j]
            visible.add((i, j))
    start = -1
    for j in range(size - 1, -1, -1):
        if trees[i][j] > start:
            start = trees[i][j]
            visible.add((i, j))

for j in range(size):
    start = -1
    for i in range(size):
        if trees[i][j] > start:
            start = trees[i][j]
            visible.add((i, j))
    start = -1
    for i in range(size - 1, -1, -1):
        if trees[i][j] > start:
            start = trees[i][j]
            visible.add((i, j))

print(len(visible))
