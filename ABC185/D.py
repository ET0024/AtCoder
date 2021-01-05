N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = [0] + a + [N + 1]

a_diff = []
k = N

for i in range(len(a) - 1):
    tmp = a[i + 1] - a[i] - 1

    if tmp > 0:
        a_diff.append(tmp)

        if k > tmp:
            k = tmp

ans = 0
for diff in a_diff:
    ans += (diff // k)
    if diff % k != 0:
        ans += 1

print(ans)
