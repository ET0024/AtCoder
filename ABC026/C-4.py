N = int(input())

child = [[] for _ in range(N)]
for i in range(N - 1):
    par = int(input()) - 1
    child[par].append(i + 1)


# return i's salary
def dfs(i):
    my_child = child[i]
    if len(my_child) == 0:
        return 1
    else:
        max_s = -1
        min_s = float('inf')

        for ch in my_child:
            s = dfs(ch)
            if s > max_s:
                max_s = s
            if s < min_s:
                min_s = s

        return max_s + min_s + 1


print(dfs(0))
