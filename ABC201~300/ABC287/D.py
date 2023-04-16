s = input()
t = input()

th_left = 0
th_right = 0

for i in range(len(t)):
    if s[i] == '?' or t[i] == '?' or s[i] == t[i]:
        th_left += 1
    else:
        break

s2 = s[len(s) - len(t):]

for i in range(len(t)):
    if s2[len(t) - 1 - i] == '?' or t[len(t) - 1 - i] == '?' or s2[len(t) - 1 - i] == t[len(t) - 1 - i]:
        th_right += 1
    else:
        break

for x in range(len(t) + 1):
    l = x
    r = len(t) - x
    if l <= th_left and r <= th_right:
        print('Yes')
    else:
        print('No')
