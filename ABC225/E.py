from fractions import Fraction

n = int(input())
angles = []
for _ in range(n):
    x, y = map(int, input().split())
    if x == 1:
        # angles.append([Fraction(10 ** 10, 1), Fraction(y - 1, x)])
        angles.append([(10 ** 10, 1), (y - 1, x)])
    else:
        # angles.append([Fraction(y, x - 1), Fraction(y - 1, x)])
        angles.append([(y, x - 1), (y - 1, x)])

angles.sort(key=lambda x: Fraction(x[0][0], x[0][1]))

ans = 0
current = (0, 1)
for i, (r2, r1) in enumerate(angles):

    if r1[0]*current[1] >= current[0]*r1[1]:
        ans += 1
        current = r2

print(ans)
