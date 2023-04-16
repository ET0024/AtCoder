n = int(input())
a = list(map(int, input().split()))
a = [0] + a

ball = [0 for _ in range(n + 1)]
for i in range(n, 0, -1):
    cnt = 0
    for x in range(i, n+1, i):
        cnt += ball[x]
    if cnt % 2 != a[i]:
        ball[i] = 1

count = 0
ans = []
for i, b in enumerate(ball):
    if i > 0 and b > 0:
        count += 1
        ans.append(i)

print(count)
if count > 0:
    print(*ans)

# # debug
# for i, b in enumerate(ball):
#     if i>0:
#         cnt = 0
#         for x in range(i, n + 1, i):
#             cnt += ball[x]
#
#         print((i, cnt))
#         print('a=', a[i])