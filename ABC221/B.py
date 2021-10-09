s = list(input())
t = list(input())

if s == t:
    print('Yes')
    exit()

diff = []
for i in range(len(s)):
    if s[i] != t[i]:
        diff.append(i)

if len(diff) != 2:
    print('No')
    exit()
if abs(diff[0] - diff[1]) != 1:
    print('No')
    exit()
else:
    t[diff[0]], t[diff[1]] = t[diff[1]], t[diff[0]]
    if s == t:
        print('Yes')
        exit()

print('No')