with open('inputs/day25.in', 'r') as infile:
    lines = infile.read().splitlines()

snafu_digit_to_int = {'2':2, '1': 1, '0': 0, '-': -1,'=':-2}

def int_to_snafu(num):
    return None

def snafu_to_int(snafu):
    res = 0
    exp = 0
    for i in snafu[::-1]:
        res += snafu_digit_to_int[i] * (5 ** exp)
        exp += 1
    return res

total = sum(snafu_to_int(line) for line in lines)
# print(total)
# print(snafu_to_int('2=020-===0-1===2=020'))

def decimal_to_quinary(num):
    res = ''
    q,r = divmod(num, 5)
    while q or r:
        res = str(r) + res
        num = q
        q,r = divmod(num, 5)
    return res

print([snafu_to_int(line) for line in lines])
for i in range(1, 23):
    print(decimal_to_quinary(i))