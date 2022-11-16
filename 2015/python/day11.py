with open('inputs/day11.in', 'r') as infile:
    password = infile.readline()


def increment(password):
    lst = list(password)
    ind = len(password) - 1
    carry = lst[ind] == 'z'
    lst[ind] = 'a' if carry else chr(ord(lst[ind])+1)
    while ind >= 0 and carry:
        ind -= 1
        carry = lst[ind] == 'z'
        lst[ind] = 'a' if carry else chr(ord(lst[ind])+1)
    return ''.join(lst)


def valid(password):
    return inc_3(password) and pairs(password) and no_banned_letters(password)


def inc_3(password):
    for i in range(len(password) - 2):
        a, b, c = map(ord, password[i:i+3])
        if c - b == 1 and b - a == 1:
            return True

    return False


def no_banned_letters(password):
    bans = 'iol'
    return not any(i in password for i in bans)


def pairs(password):
    pairs = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs += 1
            i += 1
        i += 1
    return pairs >= 2


password = increment(password)
while not valid(password):
    password = increment(password)
print(password)

password = increment(password)
while not valid(password):
    password = increment(password)
print(password)
