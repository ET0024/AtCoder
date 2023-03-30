r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))
board_after = [[''] * c for _ in range(r)]

# simulation
for x in range(r):
    for y in range(c):

        if board[x][y] != '#':
            board_after[x][y] = '.'
            continue
        board_after[x][y] = '#'
        for i in range(r):
            for j in range(c):
                if board[i][j] == '.' or board[i][j] == '#':
                    continue
                pow = int(board[i][j])
                if abs(x-i)+abs(y-j) <= pow:
                    board_after[x][y] = '.'

for r in board_after:
    print(*r, sep="")