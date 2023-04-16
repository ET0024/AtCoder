s = input()
t = input()

si = 0
ti = 0

while ti < len(t):
    if si >= len(s):
        si -= 1
    if s[si] == t[ti]:
        si += 1
        ti += 1
    else:
        si -= 1

        if si > 0 and s[si - 1] == s[si] == t[ti]:
            si += 1
            ti += 1
        else:
            print('No')
            exit()

print('Yes')
