from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x - 1, a))

# サイクルを求める
d = defaultdict(list)

time = 0
current = 0
d[current].append(time)
while True:
    time += 1
    current = a[current]
    d[current].append(time)
    if len(d[current]) > 1:
        break

offset = d[current][0]
cycle = d[current][1] - d[current][0]

if k > offset:
    k -= offset
    k %= cycle
else:
    current = 0

# simulation
for _ in range(k):
    current = a[current]

print(current + 1)
