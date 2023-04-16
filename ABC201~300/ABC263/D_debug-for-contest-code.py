n, l, r = map(int, input().split())
a = list(map(int, input().split()))

diff_l = [0 for _ in range(n)]
diff_l_min = [0 for _ in range(n)]
diff_l[0] = l - a[0]
diff_l_min[0] = diff_l[0]

for i in range(1, n):
    diff_l[i] = diff_l[i - 1] + l - a[i]
    diff_l_min[i] = min(diff_l_min[i - 1], diff_l[i])

# right
diff_r = [0 for _ in range(n)]
diff_r_min = [0 for _ in range(n)]
diff_r[0] = r - a[n - 1]
diff_r_min[0] = diff_r[0]

for i in range(1, n):
    diff_r[i] = diff_r[i - 1] + r - a[n - 1 - i]
    diff_r_min[i] = min(diff_r_min[i - 1], diff_r[i])

ans_diff = min(diff_l_min[n - 1], diff_r_min[n - 1])

for i in range(n - 1):
    tmp = min(0, diff_l_min[i]) + min(0, diff_r_min[n - 2 - i])
    if ans_diff > tmp:
        ans_diff = tmp

print(sum(a) + ans_diff)
