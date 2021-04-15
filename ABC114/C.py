N = int(input())

count = 0

def dfs(x):
    global count
    s = str(x)

    if x <= N:
        if '7' in s and '5' in s and '3' in s:
            count += 1

        dfs(10 * x + 7)
        dfs(10 * x + 5)
        dfs(10 * x + 3)

dfs(7)
dfs(5)
dfs(3)
print(count)