n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

for row in range(n):
    if row == 0:
        for col in range(m):
            if b[row][col] % 7 == 0 and col < m - 1:
                print('No')
                exit()
            if col > 0:
                if b[row][col] != b[row][col - 1] + 1:
                    print('No')
                    exit()
    else:
        for col in range(m):
            if b[row][col] != b[row - 1][col] + 7:
                print('No')
                exit()

print('Yes')
