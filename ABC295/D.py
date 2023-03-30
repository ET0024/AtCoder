from collections import defaultdict

s = list(map(int, list(input())))
n = len(s)

# これまでに現れたパターンの数を保持
ruiseki = defaultdict(int)
current_pattern = 0
ruiseki[current_pattern]+=1
for i in range(n):
    digit = s[i]
    # reverse even/odd
    if (current_pattern >> s[i]) & 1 == 0:
        current_pattern += (1 << digit)
    else:
        current_pattern -= (1 << digit)
    ruiseki[current_pattern] += 1

ans = 0
for val in ruiseki.values():
    ans += val * (val - 1) // 2

# print(ruiseki)
print(ans)
