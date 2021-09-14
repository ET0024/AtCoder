n = int(input())
a = list(map(int, input().split()))

staff = [0 for _ in range(n)]

for par in a:
    staff[par - 1] += 1

for s in staff:
    print(s)
