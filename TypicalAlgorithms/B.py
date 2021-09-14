N = int(input())

x = []
for _ in range(N):
    a, b = map(int, input().split())
    x.append((b, a))

x.sort()
current = 0
ans = 0
for end, start in x:
    if start > current:
        ans += 1
        current = end

print(ans)