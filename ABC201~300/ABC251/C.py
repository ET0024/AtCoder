from collections import defaultdict

n = int(input())
poems = []

for i in range(n):
    _s, _t = input().split()
    poems.append((_s, int(_t), i + 1))

d = defaultdict(tuple)
maxval = -1

for poem in poems:
    s, t, i = poem

    if s not in d:
        d[s] = (t, i)
        if t > maxval:
            maxval = t
    if s in d:
        if i < d[s][1]:
            d[s] = (t, i)
            if t > maxval:
                maxval = t

ans = 10 ** 7
for k, v in d.items():
    if v[0] == maxval and v[1] < ans:
        ans = v[1]

print(ans)
