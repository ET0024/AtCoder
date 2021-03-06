n = int(input())

ans = 1E10
for _ in range(n):
    a, p, x = map(int, input().split())

    if x - a > 0:
        if p < ans:
            ans = p

if ans > 1E9:
    print(-1)
else:
    print(ans)
