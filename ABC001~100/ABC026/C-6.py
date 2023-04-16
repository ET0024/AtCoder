import sys

sys.setrecursionlimit(10 ** 9)


def salary(person):
    if len(buka[person]) == 0:
        return 1
    else:
        values = []
        for staff in buka[person]:
            values.append(salary(staff))
        return max(values) + min(values) + 1


n = int(input())
buka = [[] for _ in range(n)]
for child in range(n - 1):
    child += 1
    parent = int(input())
    parent -= 1
    buka[parent].append(child)

print(salary(0))
