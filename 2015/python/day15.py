with open('inputs/day15.in', 'r') as infile:
    ingredients = {}
    for line in infile.readlines():
        ingredient, properties = line.split(': ')
        properties = properties.split(', ')
        properties = {k: int(v)
                      for k, v in map(lambda x: x.split(), properties)}
        ingredients[ingredient] = properties


def total_score(counts, count_calories):
    res = 1
    values = ingredients.values()
    calories = sum(value['calories']*counts[i]
                   for i, value in enumerate(values))
    if count_calories and calories != 500:
        return 0

    for prop in props[:-1]:
        prop_value = sum(value[prop]*counts[i]
                         for i, value in enumerate(values))
        res *= 0 if prop_value < 0 else prop_value
    return res


props = ['capacity', 'durability', 'flavor', 'texture', 'calories']
total_ingredients = 100

res = 0
# 4 ingredients
for i in range(total_ingredients + 1):
    for j in range(total_ingredients - i + 1):
        for k in range(total_ingredients - i - j + 1):
            l = total_ingredients - i - j - k
            res = max(res, total_score((i, j, k, l), count_calories=False))
print(res)

res = 0
# 4 ingredients
for i in range(total_ingredients + 1):
    for j in range(total_ingredients - i + 1):
        for k in range(total_ingredients - i - j + 1):
            l = total_ingredients - i - j - k
            res = max(res, total_score((i, j, k, l), count_calories=True))
print(res)
