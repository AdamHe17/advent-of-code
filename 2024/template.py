from collections import defaultdict
from itertools import combinations


with open("day9.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    grid = [[i for i in line] for line in lines]


def _gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = _gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def crt(nums, rems):
    prod = 1
    for n in nums:
        prod *= n

    result = 0
    for i in range(len(nums)):
        prod_i = prod // nums[i]
        _, inv_i, _ = _gcd_extended(prod_i, nums[i])
        result += rems[i] * prod_i * inv_i

    return result % prod


# Example Usage
nums1 = [5, 7]
rems1 = [1, 3]
print("x is", crt(nums1, rems1))

nums2 = [3, 4, 5]
rems2 = [2, 3, 1]
print("x is", crt(nums2, rems2))
