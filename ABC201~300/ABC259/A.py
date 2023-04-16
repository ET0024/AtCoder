n, m, x, t, d = map(int, input().split())

size = [t - d * (x-i) for i in range(x + 1)]
print(size[min(m, x)])
