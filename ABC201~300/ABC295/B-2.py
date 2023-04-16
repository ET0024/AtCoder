r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

after_board = [[''] * c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if board[x][y] != '#':
            after_board[x][y] = '.'
            continue
        else:
            after_board[x][y] = '#'
            for i in range(r):
                for j in range(c):
                    if board[i][j] not in ['.', '#']:
                        pow = int(board[i][j])
                        if abs(x-i) + abs(y-j) <= pow:
                            after_board[x][y] = '.'

for row in after_board:
    print(*row, sep='')