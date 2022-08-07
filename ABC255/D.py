import bisect

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

acc_left = [a[0]]
acc_right = [a[-1]]

for i in range(1, n):
    acc_left.append(acc_left[i - 1] + a[i])
    acc_right.append(acc_right[i - 1] + a[n - 1 - i])

for _ in range(q):
    x = int(input())
    idx = bisect.bisect_right(a, x)
    # print('----------idx', idx)
    if idx <= 0:
        print(acc_left[-1] - n * x)
    elif idx > n - 1:
        print(-acc_left[-1] + n * x)
    else:
        # print(acc_left[idx - 1])
        # print(acc_right[n - 1 - idx])
        # print(abs(n - 2 * idx) * x)
        print(-acc_left[idx - 1] + acc_right[n - 1 - idx] - (n - 2 * idx) * x)
