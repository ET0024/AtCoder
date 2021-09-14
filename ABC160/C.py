k, n = map(int, input().split())
a = list(map(int, input().split()))

# dist[i] for distance between i and i+1
dist = [-1 for _ in range(n)]
for i in range(n - 1):
    dist[i] = a[i + 1] - a[i]

dist[n - 1] = k + a[0] - a[n - 1]
print(k - max(dist))
