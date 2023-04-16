from collections import defaultdict


def calc(x, y):
    l = min(len(x), len(y))
    ans = 0
    for j in range(l):
        if x[j] == y[j]:
            ans += 1
    return ans


n = int(input())
s = []
for _ in range(n):
    s.append(input())

s_sorted = sorted(s)
d = defaultdict(int)
for i, _s in enumerate(s_sorted):
    d[_s] = i

for i, target in enumerate(s):
    idx_target = d[target]
    if idx_target == 0:
        val = calc(target, s_sorted[idx_target + 1])
        print(val)
    elif idx_target == n - 1:
        val = calc(target, s_sorted[idx_target - 1])
        print(val)
    else:
        val = max(calc(target, s_sorted[idx_target + 1]), calc(target, s_sorted[idx_target - 1]))
        # print('debug:', target, s_sorted[idx_target + 1], s_sorted[idx_target - 1])
        print(val)

