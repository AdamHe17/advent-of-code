row, col = 2981, 3075
row, col = 1, col + row - 1
target = col * (col + 1) // 2 - 2980

start = 20151125
for i in range(target - 1):
    _, start = divmod(start * 252533, 33554393)
    if i % 100000 == 0:
        print(i // 100000)

print(start)