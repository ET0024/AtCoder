from collections import defaultdict

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
ruiseki = [0 for _ in range(n+1)]
ruiseki[0] = 0
d = defaultdict(bool)
d[ruiseki[0]] = True
for i in range(1, n+1):
    ruiseki[i] = ruiseki[i - 1] + a[i-1]
    d[ruiseki[i]] = True

# print(a)
# print(ruiseki)
# print(d)

for x in range(n+1):
    base = ruiseki[x]
    if d[base + p] and d[base + p + q] and d[base + p + q + r]:
        print('Yes')
        exit()

print('No')
