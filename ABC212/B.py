s = input()
x0 = int(s[0])
x1 = int(s[1])
x2 = int(s[2])
x3 = int(s[3])


if x0 == x1 == x2 == x3:
    print('Weak')
elif (x0+1)%10 == x1 and (x1+1)%10 == x2 and(x2+1)%10 == x3:
    print('Weak')
else:
    print('Strong')
