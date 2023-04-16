h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        digit = int(s[i][j] == "#") + int(s[i + 1][j] == "#") + int(s[i][j + 1] == "#") + int(s[i + 1][j + 1] == "#")
        if digit % 2 == 1:
            ans += 1

print(ans)
