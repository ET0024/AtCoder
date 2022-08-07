n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0

while len(a) >= k:
    offset = a[k - 1]
    ans += offset
    for org in range(0, k):
        a[org] -= offset
    a.sort(reverse=True)
    a.pop()

print(ans)
