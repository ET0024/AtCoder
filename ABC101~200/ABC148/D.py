n = int(input())
a = list(map(int, input().split()))

count = 0
for val in a:
    if val == count + 1:
        count += 1

ans = n - count
if ans == n:
    print(-1)
else:
    print(ans)
