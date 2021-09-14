import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = bisect.bisect_left(A, K)
if ans >= N:
    print(-1)
else:
    print(ans)
