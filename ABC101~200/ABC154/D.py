n, k = map(int, input().split())
p = list(map(int, input().split()))

acc_sum = []
acc_sum.append(sum(p[:k]))

for i in range(k, n):
    acc_sum.append(acc_sum[-1] + p[i] - p[i - k])

print((max(acc_sum) + k) / 2)
