n = int(input())
a = list(map(int, input().split()))

a_s = set(a)
if len(a) == len(a_s):
    print('YES')
else:
    print('NO')
