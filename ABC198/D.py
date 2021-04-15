import itertools
import copy

s1 = input()
s2 = input()
s3 = input()


charset = list(set(s1+s2+s3))
l = len(charset)

if l > 10:
    print('UNSOLVABLE')
    exit()

nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
pattern = list(itertools.permutations(nums, len(charset)))

for p in pattern:
    ss1 = copy.copy(s1)
    ss2 = copy.copy(s2)
    ss3 = copy.copy(s3)
    for i, num in enumerate(p):
        ss1 = ss1.replace(charset[i], num)
        ss2 = ss2.replace(charset[i], num)
        ss3 = ss3.replace(charset[i], num)

    if ss1[0] == '0' or ss2[0] == '0' or ss3[0] == '0':
        continue

    if int(ss1) + int(ss2) == int(ss3):
        print(ss1)
        print(ss2)
        print(ss3)
        exit()

print('UNSOLVABLE')
