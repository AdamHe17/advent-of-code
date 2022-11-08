infile = open('inputs/day7.in', 'r')
lines = infile.read()

numbers = [int(i) for i in lines.split(',')]
numbers.sort()

a, b = min(numbers), max(numbers)

least = (-1, 1000000000)
for i in range(a, b + 1):
    t = sum(abs(j - i) * (abs(j - i) + 1) // 2 for j in numbers)
    if t < least[1]:
        least = (i, t)

print(least)