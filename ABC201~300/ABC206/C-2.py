from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for x in a:
    d[x] += 1

ng_count = 0
for k, v in d.items():
    if v >= 2:
        ng_count += v * (v - 1) // 2

print(n * (n - 1) // 2 - ng_count)
