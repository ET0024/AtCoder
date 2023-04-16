n, k = map(int, input().split())
a = list(map(int, input().split()))

base_num = k // n
k -= (k // n) * n

if k == 0:
    for _ in range(n):
        print(base_num)
    exit()

target = sorted(a)[k - 1]

for i in range(n):
    if a[i] <= target:
        print(base_num + 1)
    else:
        print(base_num)
