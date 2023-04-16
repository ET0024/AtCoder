n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

p -= 1
q -= 1
r -= 1
s -= 1
print(*(a[:p]+a[r:s+1]+a[q+1:r]+a[p:q+1]+a[s+1:]))