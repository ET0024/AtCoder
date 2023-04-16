n, k = map(int, input().split())
h = list(map(int, input().split()))

if len(h) <= k:
    print(0)
    exit()

h = sorted(h)[:len(h) - k]
print(sum(h))
