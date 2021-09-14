n = int(input())
s, s2 = set(), set()
for _ in range(n):
    _s = input()
    s.add(_s)
    s2.add('!' + _s)

s3 = s.intersection(s2)
if len(s3) > 0:
    print(s3.pop()[1:])
else:
    print('satisfiable')
