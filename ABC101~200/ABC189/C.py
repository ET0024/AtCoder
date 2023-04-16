n = int(input())
a = list(map(int, input().split()))






a_max = max(a)
ans = 0

for x in range(1, a_max + 1):
    local_max = 0
    for i in range(n):
        if a[i] >= x:
            local_max += x
            if local_max > ans:
                ans = local_max
        else:
            local_max = 0

print(ans)