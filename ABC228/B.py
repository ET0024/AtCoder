n, x = map(int, input().split())
a = list(map(int, input().split()))

known = [False for _ in range(n + 1)]

current = x
known[x] = True
for _ in range(n):
    current = a[current - 1]
    known[current] = True

print(known.count(True))
