n, a, b = map(int, input().split())
s = input()


def score(str):
    l = len(str)
    ret = 0
    for i in range(n):
        if i >= l - i:
            break
        if str[i] != str[l - 1 - i]:
            ret += 1
    return ret


ans = n * (a + b)
for x in range(n):
    ss = s[x:] + s[:x]
    ss_score = a * x + b * score(ss)
    if ss_score < ans:
        ans = ss_score

print(ans)
