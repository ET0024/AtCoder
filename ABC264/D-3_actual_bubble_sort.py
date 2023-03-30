from collections import defaultdict

s = input()
n = len(s)
d = defaultdict(int)
for i, c in enumerate(list('atcoder')):
    d[c] = i

s2 = [d[s[i]] for i in range(n)]

count = 0
for _ in range(n):
    for i in range(n - 1):
        if s2[i] > s2[i + 1]:
            s2[i], s2[i + 1] = s2[i + 1], s2[i]
            count += 1

print(count)
