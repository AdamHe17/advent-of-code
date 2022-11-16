import json

with open('inputs/day12.in', 'r') as infile:
    data = json.load(infile)


def sum_json(data):
    if not data or isinstance(data, str):
        return 0

    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_json(i) for i in data)
    else:
        total = 0
        if 'red' in data.keys() or 'red' in data.values():
            return 0

        for k, v in data.items():
            total += sum_json(k)
            total += sum_json(v)
        return total


print(sum_json(data))
