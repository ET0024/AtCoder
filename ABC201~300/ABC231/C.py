import bisect

N, Q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a_acc = []
count = 1
for val in a:
    a_acc.append((val, count))
    count += 1

for _ in range(Q):
    x = int(input())
    i = bisect.bisect_left(a, x)
    if i >= len(a_acc):
        print(0)
    else:
        print(N - a_acc[i][1] + 1)
