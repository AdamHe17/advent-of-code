infile = open('inputs/day8.in', 'r')
lines = infile.readlines()

lines = list(
    map(lambda x: list(map(lambda k: k.split(), x.split(' | '))), lines))

# Part 1
print(
    sum(
        sum(1 for word in code if len(word) in [2, 3, 4, 7])
        for _, code in lines))

# Part 2
total = 0
for digits, codes in lines:
    mapping = {}

    # Find one, four, seven, eight
    one, seven, four, eight = sorted(
        [i for i in digits if len(i) in [2, 3, 4, 7]], key=lambda x: len(x))
    zero, two, three, five, six, nine = '_' * 6

    # Find nine
    nine_mask = four + [i for i in seven if i not in one][0]
    nine = [
        i for i in digits if all(j in i for j in nine_mask) and len(i) == 6
    ][0]

    # Find six, zero
    length_six = [i for i in digits if len(i) == 6]
    length_six.remove(nine)
    for i in length_six:
        for j in digits:
            if sorted(f := set(i).intersection(set(nine))) == sorted(j):
                six = i
                break

    # Find zero
    length_six.remove(six)
    zero = length_six[0]

    # Find two, three, five
    length_five = [i for i in digits if len(i) == 5]
    for i in length_five:
        if sorted(set(six).intersection(set(nine))) == sorted(i):
            five = i
            break

    length_five.remove(five)
    for i in length_five:
        if all(k in nine for k in i):
            three = i
            break

    length_five.remove(three)
    two = length_five[0]

    mapping = {
        i: v
        for i, v in zip(
            map(lambda x: ''.join(sorted(x)),
                [zero, one, two, three, four, five, six, seven, eight, nine]),
            map(str, range(10)))
    }

    total += int(''.join(mapping[''.join(sorted(code))] for code in codes))

print(total)