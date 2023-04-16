n, w = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(0)
ans = set()

for i in range(n + 2):
    for j in range(n + 2):
        for k in range(n + 2):
            if i == j or j == k or k == i:
                continue
            val = a[i] + a[j] + a[k]
            if val <= w:
                ans.add(val)

print(len(ans))
