a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
bs = [int(input()) for _ in range(n)]

res = [[False]*3 for _ in range(3)]

for b in bs:
    for i in range(3):
        for j in range(3):
            if a[i][j]==b:
                res[i][j]=True

ans = False
for i in range(3):
    if res[i][0]*res[i][1]*res[i][2]:
        ans = True

for j in range(3):
    if res[0][j]*res[1][j]*res[2][j]:
        ans = True

if res[0][0]*res[1][1]*res[2][2] or res[0][2]*res[1][1]*res[2][0]:
    ans = True

if ans:
    print('Yes')
else:
    print('No')
