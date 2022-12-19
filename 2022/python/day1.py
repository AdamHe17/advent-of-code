with open('inputs/day1.in', 'r') as infile:
    calories = [sum(int(calorie) for calorie in calories.split('\n'))
                for calories in infile.read().split('\n\n')]

print(max(calories))
print(sum(sorted(calories)[-3:]))
