n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a.append(0)

ans = 0
for i in range(n):
    ride = min(k, (i + 1) * (a[i] - a[i + 1]))
    x = ride // (i + 1)
    y = ride % (i + 1)
    ans += (i + 1) * (x * a[i] - x * (x - 1) // 2) + (a[i] - x) * y
    k -= ride
    if k == 0:
        break

print(ans)
# a[0] = 100, a[1]=80, a[2] = 60, ...の場合
# a[0]に(a[0]-a[1])=20回乗る
# a[0], a[1]に交互に2*(a[1]-a[2])=40回乗る
# ...
