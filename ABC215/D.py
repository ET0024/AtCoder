import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

factorials = set()

for div in range(2, int(math.sqrt(10 ** 5)) + 1):
    for i in range(n):
        # a[i]がdivを因数に持つ場合、取り除く
        while a[i] % div == 0:
            a[i] //= div
            factorials.add(div)

for i in range(n):
    if a[i] != 1:
        factorials.add(a[i])

factorials = sorted(list(factorials))
table = [False for i in range(m + 1)]

for f in factorials:
    y = 1
    while f * y <= m:
        table[f * y] = True
        y += 1

print(table.count(False) - 1)
for i, b in enumerate(table):
    if i >= 1 and not b:
        print(i)
