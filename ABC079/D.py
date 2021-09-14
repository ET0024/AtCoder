h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

# Warshall-Froyd
for k in range(10):
    for i in range(10):
        for j in range(10):
            if c[i][k] + c[k][j] < c[i][j]:
                c[i][j] = c[i][k] + c[k][j]

ans = 0
for row in a:
    for digit in row:
        if digit < 0:
            continue
        ans += c[digit][1]

print(ans)
