import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()
count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        idx = bisect.bisect_right(l, l[i] + l[j] - 1) - 1
        count += idx - j

print(count)
