from collections import defaultdict


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


with open('inputs/day15.in', 'r') as infile:
    sensor_dists = []
    for line in infile.read().splitlines():
        _sensors, _beacons = line.split(': ')
        *_, x, y = _sensors.split(', ')
        sx, sy = int(x.split('=')[1]), int(y.split('=')[1])
        *_, x, y = _beacons.split(', ')
        bx, by = int(x.split('=')[1]), int(y.split('=')[1])
        sensor_dists.append((sx, sy, dist(sx, sy, bx, by)))


limit = 4000000
for x in range(limit+1):
    y = 0
    while y < limit:
        for sx, sy, _dist in sensor_dists:
            proj = _dist - abs(sx - x)
            if sy - proj <= y <= sy + proj:
                y = sy + proj + 1
                break
        else:
            print(f'found coordinate {x}, {y}')
            print(x * limit + y)
            1/0
