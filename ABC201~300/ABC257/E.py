N = int(input())
c = list(map(int, input().split()))

mini = min(c)
for i in reversed(range(9)):
    if c[i] == mini:
        mini_idx = i

ans = 0
for i in range(9):
    n = N
    x = 0
    if c[i] > n:
        continue

    n -= c[i]
    x = x * 10 + (i + 1)

    while n > mini:
        n -= mini
        x = x * 10 + (mini_idx + 1)

    if x > ans:
        ans = x

print(ans)
