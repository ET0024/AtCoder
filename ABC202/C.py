n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = []
for i in range(n):
    d.append(b[c[i] - 1])

count_a = [0 for _ in range(n + 1)]
count_d = [0 for _ in range(n + 1)]

for i in range(n):
    count_a[a[i]] += 1
    count_d[d[i]] += 1

ans = 0
for i in range(n + 1):
    ans += count_a[i] * count_d[i]

print(ans)
