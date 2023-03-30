L, N1, N2 = map(int, input().split())

code1 = []
code2 = []
for _ in range(N1):
    v, l = map(int, input().split())
    code1.append((v, l))
for _ in range(N2):
    v, l = map(int, input().split())
    code2.append((v, l))

idx1, pos1, idx2, pos2 = 0, 0, 0, 0
ans = 0
while True:
    v1, l1 = code1[idx1]
    v2, l2 = code2[idx2]

    # check for scope overlap
    if pos1 <= pos2 + l2 and pos2 <= pos1 + l1:
        if v1 == v2:
            ans += min(pos1 + l1, pos2 + l2) - max(pos1, pos2)
            # print('debug', pos1, l1, pos2, l2)
            # print('debug:ans=',ans)
    # search for next
    if pos1 + l1 < pos2 + l2:
        idx1 += 1
        pos1 = pos1 + l1
    elif pos1 + l1 > pos2 + l2:
        idx2 += 1
        pos2 = pos2 + l2
    else:
        idx1 += 1
        pos1 = pos1 + l1
        idx2 += 1
        pos2 = pos2 + l2
    if idx1 >= N1 or idx2 >= N2:
        break

print(ans)
