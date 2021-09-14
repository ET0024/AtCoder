n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
r = -1
total = 0
for l in range(n):

    # 左端を動かしたことによるtotalの補正
    if l > 0:
        total -= a[l - 1]

    # 累積和がk以上になるまでrを進める
    while total < k and r < n - 1:
        r += 1
        total += a[r]

    if total >= k:
        count += (n-1) - (r-1)

print(count)