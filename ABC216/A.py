s = input()
x = int(s[:-2])
y = int(s[-1])

if 0 <= y <= 2:
    print(str(x) + '-')
elif 3 <= y <= 6:
    print(x)
else:
    print(str(x) + '+')
