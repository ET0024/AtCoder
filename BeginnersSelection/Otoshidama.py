n, total = map(int, input().split())

x, y, z = -1, -1, -1

for i in range(n+1):
    for j in range(n+1-i):
        if 10000*i + 5000*j + 1000*(n-i-j) == total:
            x, y, z = i, j, n-i-j

print(x, y, z)
