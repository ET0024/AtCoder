import string

alphs = ['a']
for row in range(8):
    s = list(input())
    if '*' in s:
        print(string.ascii_lowercase[s.index('*')], 8 - row, sep='')
