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
    if len(row) < curr + 1:
        pass
    else:
        part = row[:curr + 1]
        if '.' in part[:curr] or part[-1] == '#':
            pass
        else:
            res += consume(row[curr+1:], nums[1:])

    if row[0] == '?':
        res += consume(row[1:], nums)
    
    return res

print(sum(consume(row+'.', tuple(nums)) for row, nums in ls1))
print(sum(consume(row+'.', tuple(nums)) for row, nums in ls2))
