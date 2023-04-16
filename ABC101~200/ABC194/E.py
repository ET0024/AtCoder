n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * (n + 1)

# countの初期化
a_initial = a[:m]
minvalue = n
for i in a_initial:
    count[i] += 1

for i, val in enumerate(count):
    if val == 0:
        minvalue = i
        break

for i in range(0, n - m):
    count[a[i]] -= 1
    count[a[m + i]] += 1
    if count[a[i]] == 0 and a[i] < minvalue:
        minvalue = a[i]

print(minvalue)