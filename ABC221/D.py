from collections import defaultdict

n = int(input())
a = []
b = []
days = set()
for _ in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)
    days.add(_a)
    days.add(_a + _b)

days = sorted(list(days))
days_index = defaultdict(int)
for i, val in enumerate(days):
    days_index[val] = i

count = [0 for _ in range(len(days))]
for i in range(n):
    count[days_index[a[i]]] += 1
    count[days_index[a[i] + b[i]]] -= 1

ans = [0 for _ in range(n + 1)]
ruiseki = 0
for i in range(len(days) - 1):
    ruiseki += count[i]
    ans[ruiseki] += days[i + 1] - days[i]

ans2 = []
for i in range(1, n + 1):
    ans2.append(ans[i])

print(*ans2)