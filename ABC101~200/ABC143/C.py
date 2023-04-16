n = int(input())
s = input()

count = 0
for i, c in enumerate(s):
    if i == 0:
        current = s[0]
        count += 1
    else:
        if c == current:
            continue
        else:
            current = c
            count += 1

print(count)
