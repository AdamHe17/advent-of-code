infile = open('inputs/day6.in', 'r')
line = infile.readline()
fishes = {i: line.count(str(i)) for i in range(9)}


def next_state(fishes):
    new_state = {}
    for i, v in fishes.items():
        if i == 0:
            continue

        new_state[i - 1] = fishes[i]

    new_state[8] = fishes[0]
    new_state[6] += fishes[0]

    return new_state


for _ in range(256):
    fishes = next_state(fishes)

print(sum(v for k, v in fishes.items()))