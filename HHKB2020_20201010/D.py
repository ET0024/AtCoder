def count_box(w, h, b):
    return max(0, w - b + 1) * max(0, h - b + 1)


t = int(input())

for testno in range(t):
    n, a, b = map(int, input().split())

    print("square1", (n-a+1)**2)
    print("square2", (n-b+1)**2)

    tmp = (-3*a*a + (2*n+3)*a + 2)/2
    print(tmp**2)
    print("ans", (n-a+1)**2 * (n-b+1)**2 - tmp**2)

    # tmp = ((-3*a*a + (2*n+1)*a)/2)**2
    print("tmp", tmp)
    #
    # print("debug:", n, a, b)
    # count = 0
    # for i in range(n-a+1):
    #     for j in range(n-a+1):
    #         print("(i,j)", i,j)
    #         print("n-j-a", n-j-a)
    #         count += count_box(i, j+a, b)
    #         count += count_box(i+a, n-j-a, b)
    #         count += count_box(n-i, j, b)
    #         count += count_box(n-i-a, n-j, b)
    #         print("count",count)
    # print("ans",count)
    # break
