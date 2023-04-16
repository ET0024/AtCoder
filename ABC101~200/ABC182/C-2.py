s = input()

if len(s) == 1:
    if int(s) % 3 == 0:
        print(0)
        exit()
    else:
        print(-1)
        exit()
if len(s) == 2:
    if int(s) % 3 == 0:
        print(0)
        exit()
    elif int(s[0]) % 3 == 0 or int(s[1]) % 3 == 0:
        print(1)
        exit()
    else:
        print(-1)
        exit()

mod1 = s.count('1') + s.count('4') + s.count('7')
mod2 = s.count('2') + s.count('5') + s.count('8')
mod0 = s.count('3') + s.count('6') + s.count('9')
mod = (mod1 + 2 * mod2) % 3

if mod == 0:
    print(0)
    exit()
elif mod == 1:
    if mod1 >= 1:
        print(1)
        exit()
    elif mod2 >= 2:
        print(2)
        exit()
elif mod == 2:
    if mod2 >= 1:
        print(1)
        exit()
    elif mod1 >= 2:
        print(2)
        exit()

print(-1)
