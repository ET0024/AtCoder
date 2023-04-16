import bisect
L, Q = map(int, input().split())
cut = [0, L]

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(cut, x)
    else:
        idx = bisect.bisect_left(cut, x)
        print(cut[idx] - cut[idx - 1])
