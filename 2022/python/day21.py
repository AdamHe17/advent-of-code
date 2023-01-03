import operator

with open('inputs/day21.in') as infile:
    _dict = {}
    for line in infile.read().splitlines():
        key, value = line.split(': ')
        if value.isdigit():
            _dict[key] = int(value)
        else:
            v1, op, v2 = value.split()
            _dict[key] = (v1, op, v2)

operations = {'+':operator.add, '-': operator.sub, '*': operator.mul, '/':operator.floordiv, '=':operator.eq}

def get_value(key):
    value = _dict[key]
    if isinstance(value, int):
        return value
    else:
        v1, op, v2 = value
        value1 = get_value(v1)
        value2 = get_value(v2)
        if key == 'root':
            print(value1)
            print(value2)
        return operations[op](value1, value2)


target_key = 'root'
for i in range(3_352_886_130_000, 3_352_886_200_000):
    _dict['humn'] = i
    if get_value(target_key):
        print(i)
        1/0