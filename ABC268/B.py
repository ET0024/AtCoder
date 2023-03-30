s = input()
t = input()

if len(s) > len(t):
    print('No')
    exit()

t = t[:len(s)]
if s == t:
    print('Yes')
else:
    print('No')