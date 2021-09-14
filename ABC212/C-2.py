n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = float('inf')

i = 0
j = 0
while i < n and j < m:  # あとで条件
    ans = min(ans, abs(a[i] - b[j]))
    if a[i] > b[j]:
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        break

print(ans)
