p = list(map(int, input().split()))
ans = []
s = 'abcdefghijklmnopqrstuvwxyz'
for x in p:
    ans.append(s[x-1])

print(''.join(ans))