n = int(input())
child = [[] for _ in range(n)]

for i in range(1, n):
    b = int(input())
    child[b - 1].append(i)


def salary(i):
    if len(child[i]) == 0:
        return 1
    else:

        tmp = []
        for c in child[i]:
            tmp.append(salary(c))

        return max(tmp) + min(tmp) + 1


print(salary(0))
