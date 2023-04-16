n = int(input())
s = list(input())

start = s[0]
for i, attr in enumerate(s):
    if i%2 == 0 and attr != start or i%2 != 0 and attr == start:
        print('No')
        exit()

print('Yes')