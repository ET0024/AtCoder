p = list(map(int, input().split()))
s = 'abcdefghijklmnopqrstuvwxyz'
ans = []
for i in range(len(p)):
    ans.append(s[p[i] - 1])

print(''.join(ans))
