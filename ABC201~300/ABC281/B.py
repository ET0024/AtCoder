import string
alphs = string.ascii_letters[26:]

s = input()
pre = s[0]
mid = s[1:-1]
post = s[-1]

if len(s) != 8:
    print('No')
    exit()
if pre in alphs and post in alphs and mid.isdigit():
    mid_num = int(mid)
    if 100000 <= mid_num <= 999999:
        print('Yes')
        exit()

print("No")
