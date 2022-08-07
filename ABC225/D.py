N, Q = map(int, input().split())

state = [[i, -1] for i in range(N)]  # (previous node, next node)
for _ in range(Q):
    query = input()

    if query[0] == '1':
        _, x, y = query.split()
        x = int(x) - 1
        y = int(y) - 1
        state[x][1] = y
        state[y][0] = x
    elif query[0] == '2':
        _, x, y = query.split()
        x = int(x) - 1
        y = int(y) - 1
        state[x][1] = -1
        state[y][0] = y
    else:
        _, x = query.split()
        x = int(x) - 1

        while state[x][0] != x:
            x = state[x][0]  # move to previous node
        lst = [x + 1]
        count = 1

        while state[x][1] != -1:
            count += 1
            x = state[x][1]  # move to next node
            lst.append(x + 1)
        print(count, *lst)
