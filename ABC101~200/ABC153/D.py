import math

h = int(input())

ans = 0
monster = 1

while h > 1:
    ans += monster
    monster *= 2
    h = h // 2

ans += monster
print(ans)
