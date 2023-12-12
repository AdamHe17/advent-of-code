with open("day4.in", "r") as infile:
    lines = infile.readlines()

# res = 0
# for line in lines:
#     line = line.split(':')[1]
#     winning, nums = line.split(' | ')
#     winning = [int(i) for i in winning.split()]
#     nums = [int(i) for i in nums.split()]
#     res += 2 ** sum(1 for i in nums if i in winning)//2

# print(res)

counts = {i: 1 for i in range(len(lines))}
res = 0
for i, line in enumerate(lines):
    line = line.split(':')[1]
    winning, nums = line.split(' | ')
    winning = [int(i) for i in winning.split()]
    nums = [int(i) for i in nums.split()]
    matches = sum(1 for i in nums if i in winning)
    for j in range(matches):
        if i + j + 1 in counts:
            counts[i+j+1] += counts[i]
    res += counts[i]
print(res)