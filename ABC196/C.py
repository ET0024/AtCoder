s = input()
l = len(s)

if l == 1:
    print(0)
    exit()

n1 = int(s[:l // 2])
n2 = int(s[l // 2:])

count = 0
for k in range(1, l // 2 + 1):
    if k < l / 2:
        count += 9 * (10 ** (k - 1))
    else:
        if n1 > n2:
            count += n1 - 10 ** (k - 1)
        else:
            count += n1 - 10 ** (k - 1) + 1

print(count)
