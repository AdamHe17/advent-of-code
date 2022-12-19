with open('inputs/day8.in', 'r') as infile:
    lines = infile.readlines()
    trees = []
    for line in lines:
        trees.append([int(i) for i in line.strip()])

# Part 1
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

# Part 2
_max = -1
scenic_scores = [[-1] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        me = trees[i][j]
        score = 1

        # print(i, j)
        r = i - 1
        count = 0
        while r >= 0:
            count += 1
            if trees[r][j] >= me:
                break
            r -= 1
        score *= count
        # print(count)

        r = i + 1
        count = 0
        while r < size:
            count += 1
            if trees[r][j] >= me:
                break
            r += 1
        score *= count
        # print(count)

        c = j - 1
        count = 0
        while c >= 0:
            count += 1
            if trees[i][c] >= me:
                break
            c -= 1
        score *= count
        # print(count)

        c = j + 1
        count = 0
        while c < size:
            count += 1
            if trees[i][c] >= me:
                break
            c += 1
        score *= count
        _max = max(score, _max)


class ScenicScore:
    def __init__(self, height: int):
        self.left = 0
        self.up = 0
        self.down = 0
        self.right = 0
        self.height = height

    def get_score(self):
        return self.left * self.right * self.up * self.down


scenic_scores = [[ScenicScore(trees[i][j])
                  for j in range(size)] for i in range(size)]
scenic_scores = [[1]*size for _ in range(size)]

for i in range(1, size - 1):
    tree_peaks = [0] * 10
    # iterate right
    for j in range(1, size - 1):
        curr_height = trees[i][j]
        last_blocking_tree = tree_peaks[curr_height]
        scenic_scores[i][j] *= j - last_blocking_tree
        for k in range(curr_height):
            tree_peaks[k] = j


# iterate right then down
for i in range(1, size - 1):
    for j in range(1, size - 1):
        score = scenic_scores[i][j]
        above_tree = trees[i - 1][j]
        if score.height <= above_tree:
            score.up = 1
        else:
            score.up = scenic_scores[i - 1][j].up + 1

        left_tree = trees[i][j - 1]
        if score.height <= left_tree:
            score.left = 1
        else:
            score.left = scenic_scores[i][j - 1].left + 1

# iterate left then up
for i in range(size - 2, 0, -1):
    for j in range(size - 2, 0, -1):
        score = scenic_scores[i][j]
        below_tree = trees[i + 1][j]
        if score.height <= below_tree:
            score.below = 1
        else:
            score.below = scenic_scores[i + 1][j].below + 1

        right_tree = trees[i][j + 1]
        if score.height <= right_tree:
            score.right = 1
        else:
            score.right = scenic_scores[i][j - 1].right + 1

print(_max)
