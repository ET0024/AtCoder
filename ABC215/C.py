import itertools

s, k = input().split()
k = int(k)

x = set()
for pattern in itertools.permutations(s):
    x.add(pattern)

x = sorted(list(x))
print(''.join(x[k - 1]))
