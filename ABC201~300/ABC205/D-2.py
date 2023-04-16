import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))


def position(n):
    return n - bisect.bisect_left(A, n)


# for i in range(20):
#     print(i, position(i))
#
for _ in range(Q):
    K = int(input())

    # position(n) == K となる最大のnを二分探索する
    left = 1
    right = 10 ** 18 + 10 ** 5 + 1

    while right - left > 0:
        mid = (right + left) // 2
        if position(mid) > K:
            right = mid
        else:
            left = mid + 1

    print(left - 1)
