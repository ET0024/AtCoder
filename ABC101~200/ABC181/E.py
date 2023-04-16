import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
ans = 1e16

for w in W:
    # bisect.insort(H, w)
    # tmp_sum = 0

    # store index to use H.pop(x) later
    x = bisect.bisect_left(H, w)
    H.insert(x, w)

    tmp_sum = 0
    for i in range(0, N, 2):
        tmp_sum += H[i + 1] - H[i]
    if tmp_sum < ans:
        ans = tmp_sum

    # H.remove(w)
    # improve calc cost of H.remove (O(N)) to H.pop (O(1))
    H.pop(x)

print(ans)
