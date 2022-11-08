from pprint import pprint

infile = open('inputs/day13.in', 'r')
coords, folds = infile.read().split('\n\n')

coords = list(map(lambda x: tuple(map(int, x.split(','))), coords.split('\n')))

# Part 1

x_fold, y_fold = [], []
first_fold = None
for fold in folds.split('\n'):
    *_, fold = fold.split(' ')
    axis, value = fold.split('=')
    value = int(value)
    if not first_fold:
        first_fold = (axis, value)
    if axis == 'x':
        x_fold.append(value)
    else:
        y_fold.append(value)

if first_fold[0] == 'x':
    folded = [(x, y) if x < first_fold[1] else (2 * first_fold[1] - x, y)
              for x, y in coords]
else:
    folded = [(x, y) if y < first_fold[1] else (x, 2 * first_fold[1] - y)
              for x, y in coords]

print(len(set(folded)))

# Part 2

folded = coords[:]
for fold in x_fold:
    folded = [(x, y) if x < fold else (2 * fold - x, y) for x, y in folded]
for fold in y_fold:
    folded = [(x, y) if y < fold else (x, 2 * fold - y) for x, y in folded]

print(x_fold[-1], y_fold[-1])

m = [['.'] * (x_fold[-1] + 1) for i in range(y_fold[-1] + 1)]
for x, y in set(folded):
    m[y][x] = '@'
m = list(map(lambda x: ''.join(x), m))
pprint(m)