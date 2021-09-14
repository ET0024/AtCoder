import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))


def position(A, x):
    # 正整数xが何番目かを返す
    idx = bisect.bisect_left(A, x)
    return x - idx


for _ in range(Q):
    K = int(input())

    left = 1
    right = 10 ** 19

    while right - left > 0:
        mid = (right + left) // 2
        pos = position(A, mid)

        if pos > K:
            right = mid
        else:
            left = mid + 1

    target = right - 1
    print(target)

    # print('found position:', pos, 'K:', K, 'mid:', mid, 'right:', right)
    # print(mid)

# for i in range(1, 20):
#     print(i, position(A, i))