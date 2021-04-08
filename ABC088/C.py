c = [list(map(int, input().split())) for _ in range(3)]

# row check
if not (c[1][0]-c[0][0] == c[1][1]-c[0][1] == c[1][2]-c[0][2]) or \
        not (c[2][0]-c[1][0] == c[2][1]-c[1][1] == c[2][2]-c[1][2]):
    print('No')
    exit()

# column check
if not (c[0][1]-c[0][0] == c[1][1]-c[1][0] == c[2][1]-c[2][0]) or \
        not (c[0][2]-c[0][1] == c[1][2]-c[1][1] == c[2][2]-c[2][1]):
    print('No')
    exit()

print('Yes')


