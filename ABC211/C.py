from collections import defaultdict

s = input()
d = defaultdict(int)
for c in s:
    if c == 'c':
        d['c'] += 1
    elif c == 'h':
        d['h'] += d['c']
    elif c == 'o':
        d['o'] += d['h']
    elif c == 'k':
        d['k'] += d['o']
    elif c == 'u':
        d['u'] += d['k']
    elif c == 'd':
        d['d'] += d['u']
    elif c == 'a':
        d['a'] += d['d']
    elif c == 'i':
        d['i'] += d['a']

print(d['i'] % (10 ** 9 + 7))
