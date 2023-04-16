from collections import defaultdict

n = int(input())
x = []
y = []
dict_x = defaultdict(list)
for _ in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
    dict_x[_x].append(_y)

ans = 0
for xi in dict_x.keys():
    for xj in dict_x.keys():
        if xi == xj:
            continue

        count = 0
        for yi in dict_x[xi]:
            if yi in dict_x[xj]:
                count += 1

        ans += count * (count - 1) // 2

print(ans // 2)
