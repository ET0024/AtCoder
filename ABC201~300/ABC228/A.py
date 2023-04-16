s, t, x = map(int, input().split())

if s < t:
    if s <= x < t:
        print('Yes')
        exit()
elif t < s:
    if s <= x or x < t:
        print('Yes')
        exit()

print('No')
