n = int(input())
a = list(map(int, input().split()))

count = [0 for _ in range(n + 1)]
for val in a:
    count[val] += 1

total_case = 0
for c in count:
    if c >= 2:
        total_case += c * (c - 1) // 2

for k in range(1, n + 1):
    val = a[k - 1]
    c = count[val]
    if c >= 2:
        print(total_case - c * (c - 1) // 2 + (c - 1) * (c - 2) // 2)
    else:
        print(total_case)
