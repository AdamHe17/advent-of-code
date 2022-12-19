with open('inputs/day2.in', 'r') as infile:
    rounds = [[a, b] for a, b in [line.split() for line in infile.readlines()]]

beats = {'B': 'A', 'C': 'B', 'A': 'C'}


def score(opponent, me):
    me = chr(ord(me) - 23)
    return ord(me) - 64 + 3 * (opponent == me) + 6 * (beats[me] == opponent)


def score2(opponent, me):
    if me == 'X':
        return (ord(opponent) - 64 - 1 + 3) % 3 or 3
    if me == 'Y':
        return ((ord(opponent) - 64) or 3) + 3
    if me == 'Z':
        return ((ord(opponent) - 64 + 1) % 3 or 3) + 6


print(sum(score(a, b) for a, b in rounds))
print(sum(score2(a, b) for a, b in rounds))
