from functools import lru_cache

with open('day12.in', 'r') as infile:
    lines = infile.readlines()

ls1, ls2 = [], []
for line in lines:
    row, nums = line.split()
    ls1.append((row, [int(i) for i in nums.split(',')]))
    ls2.append(('?'.join([row]*5), [int(i) for i in nums.split(',')]*5))

@lru_cache
def consume(row, nums):
    if not nums:
        return 0 if '#' in row else 1

    if not row:
        return 0

    if row[0] == '.':
        return consume(row[1:], nums)

    curr = nums[0]
    res = 0
    if row[0] == '#' or row[0] == '?':
        i = 1
        while i < len(row):
            if i == curr and row[i] != '#':
                res += consume(row[i+1:], nums[1:])
                break
            if row[i] == '.':
                break
            i += 1

    if row[0] == '?':
        res += consume(row[1:], nums)

    return res

print(sum(consume(row+'.', tuple(nums)) for row, nums in ls1))
print(sum(consume(row+'.', tuple(nums)) for row, nums in ls2))