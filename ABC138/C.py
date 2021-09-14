n = int(input())
v = list(map(int, input().split()))

v.sort()
val = v[0]
for i in range(1, n):
    val = (val + v[i]) / 2

print(val)
