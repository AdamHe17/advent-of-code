from collections import defaultdict
from heapq import heappush
from bisect import bisect_left


def can_compute(nums, target):
    if len(nums) == 1:
        return int(nums[0]) == target

    if int(nums[0]) > target:
        return False

    a, b, *rest = nums
    a = str(a)
    return (
        can_compute([int(a) + int(b)] + rest, target)
        or can_compute([int(a) * int(b)] + rest, target)
        or can_compute([a + b] + rest, target)
    )


with open("day7.in", "r") as infile:
    lines = infile.readlines()

    res = 0
    for line in lines:
        target, nums = line.split(": ")

        if can_compute([i for i in nums.split(" ")], int(target)):
            res += int(target)

    print(res)
