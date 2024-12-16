from collections import defaultdict
from heapq import heappush
from bisect import bisect_left

with open("day6.in", "r") as infile:
    lines = infile.readlines()

obs_by_row: dict[int, list[int]] = defaultdict(list)
obs_by_col: dict[int, list[int]] = defaultdict(list)

start = (-1, -1)
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            heappush(obs_by_row[r], c)
            heappush(obs_by_col[c], r)

        if char == "^":
            start = (r, c)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr = start
curr_dir = 0
visited = set()
while True:
    print(curr)
    r, c = curr
    if curr_dir in [0, 2]:  # up or down
        obs_in_col = obs_by_col[c]
        ind = bisect_left(obs_in_col, r)
        print(obs_in_col, r, ind)
        if curr_dir == 2:
            if ind == len(obs_in_col):
                break
        elif curr_dir == 0:
            ind -= 1
            if ind == -1:
                break

        next_obs_row = obs_in_col[ind]
        _dir = 1 if next_obs_row > r else -1
        for nr in range(r, next_obs_row, _dir):
            visited.add((nr, c))

        curr = (next_obs_row - _dir, c)
        curr_dir = (curr_dir + 1) % 4

    elif curr_dir in [1, 3]:  # right or left
        obs_in_row = obs_by_row[r]
        ind = bisect_left(obs_in_row, c)
        if curr_dir == 1:
            if ind == len(obs_in_row):
                break
        elif curr_dir == 3:
            ind -= 1
            if ind == -1:
                break

        next_obs_col = obs_in_row[ind]
        _dir = 1 if next_obs_col > c else -1
        for nc in range(c, next_obs_col, _dir):
            visited.add((r, nc))

        curr = (r, next_obs_col - _dir)
        curr_dir = (curr_dir + 1) % 4

print(len(visited))

# res = 0
# for r, c in visited:
#     if grid[r][c] == "#":
#         continue

#     new_grid = [[i for i in line] for line in grid]
#     new_grid[r][c] = "#"
#     loop, _ = forms_loop(new_grid, curr)
#     res += loop


# print(res)
