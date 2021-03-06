import math

n = int(input())
sat_list = set()
for a in range(2, math.floor(math.sqrt(n)) + 1):
    for b in range(2, math.floor(math.log(n) / math.log(a)) + 1):
        sat_list.add(a ** b)
print(n - len(sat_list))
