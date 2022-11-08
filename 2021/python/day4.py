infile = open('inputs/day4.in', 'r')

lines = infile.read()
numbers, *lines = lines.split('\n\n')
numbers = [int(i) for i in numbers.split(',')]

boards = []
for block in lines:
    board = []
    for line in block.split('\n'):
        board += [[int(i), 0] for i in line.split()]
    boards.append(board)


def check_win(board):
    for i in range(5):
        if sum(board[i][1] for i in range(i * 5, (i + 1) * 5)) == 5:
            return True

        if sum(board[i][1] for i in range(i, 25, 5)) == 5:
            return True

    return False


index = 0
while len(boards) > 1:
    curr = numbers[index]
    for board in boards:
        for i in range(25):
            if board[i][0] == curr:
                board[i][1] = 1

    if any(check_win(board) for board in boards):
        boards = list(filter(lambda x: not check_win(x), boards))

    index += 1

last_winner = boards[0]
while not check_win(last_winner):
    curr = numbers[index]
    for i in range(25):
        if last_winner[i][0] == curr:
            last_winner[i][1] = 1
    index += 1

print(last_winner)
unmarked = sum([i[0] for i in last_winner if not i[1]])
print(unmarked, numbers[index - 1])
print(unmarked * numbers[index - 1])