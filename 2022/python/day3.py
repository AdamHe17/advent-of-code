with open('inputs/day3.in', 'r') as infile:
    sacks = [line.strip() for line in infile.readlines()]


def priority(item):
    return ord(item) - (96 * item.islower() or 38)


print(sum(map(priority, [set.intersection(
    *map(set, (sack[:len(sack) // 2], sack[len(sack) // 2:]))).pop() for sack in sacks])))
print(sum(map(priority, [set.intersection(*map(set, group)).pop()
      for group in zip(sacks[::3], sacks[1::3], sacks[2::3])])))
