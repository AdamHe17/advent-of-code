infile = open('day1.in', 'r')
masses = [int(i) for i in infile.readlines()]

print(sum(i // 3 - 2 for i in masses))

# Part 2


def get_fuel(n):
    res = 0
    while (n := n // 3 - 2) > 0:
        res += n

    return res


print(sum(get_fuel(i) for i in masses))