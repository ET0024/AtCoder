Q = int(input())
N = 1048576
a = [-1 for _ in range(N)]
jump_index = [i for i in range(N)]

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        x2 = jump_index[jump_index[jump_index[jump_index[x % N]]]]
        # x2 = x % N
        # while jump_index[x2] != x2:
        #     x2 = jump_index[x2]

        while a[x2] != -1:
            x2 = (x2 + 1) % N
            jump_index[x2] = x % N
        a[x2] = x
        jump_index[x % N] = x2
        jump_index[x2] = x2
    if t == 2:
        print(a[x % N])
