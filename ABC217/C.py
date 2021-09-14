n = int(input())
p = list(map(int, input().split()))

ans = [0 for _ in range(n)]
for i, val in enumerate(p):
    ans[val - 1] = i + 1
print(*ans)
