n = int(input())
a = list(map(int, input().split()))
a = list(map(lambda x: (x % 200), a))

for target in range(n):
    dp_b = [[False] * 200 for _ in range(n)]
    dp_c = [[False] * 200 for _ in range(n)]

    if target == 0:
        dp_b[0][a[0]] = True
        dp_c[0][0] = True
    else:
        dp_b[0][0] = True
        dp_b[0][a[0]] = True
        dp_c[0][0] = True
        dp_c[0][a[0]] = True

    for i in range(1, n):
        if i == target:
            for k in range(200):
                dp_b[i][k] = dp_b[i - 1][(k - a[i]) % 200]
                dp_c[i][k] = dp_c[i - 1][k]
        else:
            for k in range(200):
                dp_b[i][k] = dp_b[i - 1][k] or dp_b[i - 1][(k - a[i]) % 200]
                dp_c[i][k] = dp_c[i - 1][k] or dp_c[i - 1][(k - a[i]) % 200]

    for k in range(200):
        if dp_b[-1][k] and dp_c[-1][k]:
            # print(target)
            # print(k)
            # print(dp_b[-1][k])
            # print(dp_c[-1][k])
            # print(dp_b[-1])
            # print(dp_c[-1])
            print('Yes')

            # backtrace the result
            _b = k
            _c = k
            b_ans = []
            c_ans = []
            for i in reversed(range(n)):
                if i > 0:
                    if dp_b[i - 1][(_b - a[i]) % 200]:
                        b_ans.append(i + 1)
                        _b = (_b - a[i]) % 200
                    if dp_c[i - 1][(_c - a[i]) % 200]:
                        c_ans.append(i + 1)
                        _c = (_c - a[i]) % 200
                else:
                    if dp_b[0][(a[0]) % 200]:
                        b_ans.append(1)
                    if dp_c[0][(a[0]) % 200]:
                        c_ans.append(1)
                    b_ans = list(reversed(b_ans))
                    c_ans = list(reversed(c_ans))

            print(len(b_ans), *b_ans)
            print(len(c_ans), *c_ans)

            exit()

print('No')
