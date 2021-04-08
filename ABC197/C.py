n = int(input())
a = list(map(int, input().split()))

ans = float('inf')

# bit search
for pattern in range(1 << (n - 1)):

    calc_list = []
    tmp = a[0]
    # calc OR
    for i in range(n - 1):
        if (pattern >> i) & 1:
            tmp |= a[i + 1]
        else:
            calc_list.append(tmp)
            tmp = a[i + 1]
    calc_list.append(tmp)

    # calc XOR
    tmp = 0
    for calc in calc_list:
        tmp ^= calc

    # update ans
    if tmp < ans:
        ans = tmp

print(ans)
