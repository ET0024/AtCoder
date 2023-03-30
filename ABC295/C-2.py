from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for color in a:
    d[color] += 1

ans = 0
for val in d.values():
    ans += val // 2

print(ans)
