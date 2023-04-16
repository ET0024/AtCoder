s = input()

for i in range(len(s)):
    tmp = "0"*i + s

    if tmp == tmp[::-1]:
        print('Yes')
        exit()

print('No')