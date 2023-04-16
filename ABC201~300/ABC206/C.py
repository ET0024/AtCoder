from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for item in a:
    d[item] += 1

val = []
for key in d:
    val.append(d[key])

if len(val) == 1:
    print(0)
    exit()
else:
    val2 = list(map(lambda x: x**2, val))
    print((sum(val)**2 - sum(val2))//2)
