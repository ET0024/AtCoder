from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

# frequency expression (=run length)
d = defaultdict(int)
for val in a:
    d[val] += 1

# merge Cj into original cards
for _ in range(m):
    b, c = map(int, input().split())
    d[c] += b

# convert RLE to sorted list
d2 = sorted(list(d.items()), reverse=True)

# select n cards in descending order
ans = 0
rem = n
for val, freq in d2:
    ans += val * min(freq, rem)
    rem -= min(freq, rem)
    if rem == 0:
        break

print(ans)