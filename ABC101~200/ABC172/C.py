import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_acc = [0 for _ in range(n + 1)]
b_acc = [0 for _ in range(m + 1)]
for i in range(n):
    a_acc[i + 1] = a_acc[i] + a[i]

for i in range(m):
    b_acc[i + 1] = b_acc[i] + b[i]

ans = 0
for i in range(n + 1):
    if a_acc[i] > k:
        break
    # 残り (k - a_acc[i])分
    ans = max(ans, i + bisect.bisect_right(b_acc, k - a_acc[i]) - 1)

print(ans)
