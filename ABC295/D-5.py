from collections import defaultdict

s = input()
d = defaultdict(int)
pattern = 0
d[pattern] += 1
for _digit in s:
    digit = int(_digit)
    if pattern >> digit & 1 == 0:
        pattern += 1 << digit
    else:
        pattern -= 1 << digit
    d[pattern] += 1

ans = 0
for val in d.values():
    ans += val * (val - 1) // 2

print(ans)
