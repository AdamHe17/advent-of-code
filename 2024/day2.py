def is_safe(nums):
    diffs = [b - a for a, b in zip(nums, nums[1:])]
    if all(3 >= i > 0 for i in diffs) or all(-3 <= i < 0 for i in diffs):
        return True
    return False


with open("day2.in", "r") as infile:
    lines = infile.readlines()

    res = 0
    for line in lines:
        nums = list(map(int, line.split()))
        if is_safe(nums):
            res += 1
    print(res)

with open("day2.in", "r") as infile:
    lines = infile.readlines()

    res = 0
    for line in lines:
        nums = list(map(int, line.split()))
        if is_safe(nums):
            res += 1
            continue

        if any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))):
            res += 1

    print(res)
