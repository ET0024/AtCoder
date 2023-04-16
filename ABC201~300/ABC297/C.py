h, w = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(input()))

for i in range(h):
    for j in range(w - 1):
        if board[i][j] == 'T' and board[i][j + 1] == 'T':
            board[i][j] = 'P'
            board[i][j + 1] = 'C'

for i in range(h):
    print(*board[i], sep='')
