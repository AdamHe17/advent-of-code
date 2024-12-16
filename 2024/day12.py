from collections import defaultdict


def get_neighbors(coords, corners=True):
    r, c = coords
    return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)] + (
        [
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c - 1),
            (r + 1, c + 1),
        ]
        if corners
        else []
    )


def get_region(start, plant, grid):
    queue = [start]
    region = set()
    while queue:
        curr = queue.pop()
        if curr in region:
            continue

        if _map[curr] != plant:
            continue

        region.add(curr)
        for n in get_neighbors(curr, corners=False):
            queue.append(n)

    return region


def count_sides(perimeter):
    sides = 0
    p_by_row = defaultdict(list)
    p_by_col = defaultdict(list)
    for r, c in perimeter:
        p_by_row[r].append((r, c))
        p_by_col[c].append((r, c))

    for row in p_by_row.values():
        row.sort(key=lambda x: x[1])
        print(row)
        i = 0
        while i < len(row) - 1:
            start = i
            while i < len(row) - 1 and row[i][1] + 1 == row[i + 1][1]:
                i += 1

            if i > start:
                sides += 1
            else:
                i += 1

    for col in p_by_col.values():
        col.sort(key=lambda x: x[0])
        i = 0
        while i < len(col) - 1:
            start = i
            while i < len(col) - 1 and col[i][0] + 1 == col[i + 1][0]:
                i += 1

            if i > start:
                sides += 1
            else:
                i += 1

    return sides


with open("day12.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    grid = [[i for i in line] for line in lines]
    height = len(grid)
    width = len(grid[0])
    _map: dict[tuple[int, int], str] = defaultdict(
        lambda: "", {(r, c): grid[r][c] for r in range(height) for c in range(width)}
    )

    visited = set()
    regions = set()
    for r in range(height):
        for c in range(width):
            if (r, c) in visited:
                continue

            region = get_region((r, c), grid[r][c], _map)
            visited = set.union(visited, region)
            regions.add(frozenset(region))

    res = 0
    for region in regions:
        area = len(region)
        perimeter = set()
        for r, c in region:
            for nr, nc in get_neighbors((r, c)):
                if (nr, nc) not in region:
                    perimeter.add((nr, nc))

        sides = count_sides(perimeter)
        print(area, sides)
        res += area * sides

    print(res)
