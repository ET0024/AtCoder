n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a2 = [0] + a + [n + 1]
diff = []
for i in range(1, len(a2)):
    d = a2[i] - a2[i - 1] - 1
    if d > 0:
        diff.append(d)

if len(diff) == 0:
    print(0)
    exit()
diff.sort()
k = diff[0]

ans = 0
for d in diff:
    ans += (d - 1) // k + 1

print(ans)
