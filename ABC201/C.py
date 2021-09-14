s = list(input())


def valid(p):
    for i, x in enumerate(s):
        if x == 'x' and str(i) in str(p):
            return False
        elif x == 'o' and str(i) not in str(p):
            return False

    return True


count = 0
for p1 in range(10):
    for p2 in range(10):
        for p3 in range(10):
            for p4 in range(10):

                if valid(str(p1) + str(p2) + str(p3) + str(p4)):
                    count += 1

print(count)
