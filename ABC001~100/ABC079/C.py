s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

flag = False
for op1 in [-1, 1]:
    for op2 in [-1, 1]:
        for op3 in [-1, 1]:
            val = a + op1 * b + op2 * c + op3 * d
            if val == 7:
                flag =True
                break
        if flag:
            break
    if flag:
        break

op1 = str(op1).replace('-1', '-').replace('1', '+')
op2 = str(op2).replace('-1', '-').replace('1', '+')
op3 = str(op3).replace('-1', '-').replace('1', '+')

print(s[0]+op1+s[1]+op2+s[2]+op3+s[3]+'=7')