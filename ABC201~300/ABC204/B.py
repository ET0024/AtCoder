n = int(input())
a = list(map(int, input().split()))

ans = 0
for item in a:
    if item > 10:
        ans += item - 10

print(ans)
