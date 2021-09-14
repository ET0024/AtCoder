n = int(input())
a = list(map(int, input().split()))

acc = [0 for _ in range(n)]
acc_max = [0 for _ in range(n)]

for i, val in enumerate(a):
    acc[i] = acc[i - 1] + a[i]
    acc_max[i] = max(acc_max[i - 1], acc[i])

current = 0
current_max = 0
for i in range(n):
    current_max = max(current_max, current + acc_max[i])
    current += acc[i]

print(current_max)
