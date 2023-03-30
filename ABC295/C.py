from collections import defaultdict

d = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))
for color in a:
    d[color] += 1

ans = 0
for v in d.values():
    ans += v // 2

print(ans)
