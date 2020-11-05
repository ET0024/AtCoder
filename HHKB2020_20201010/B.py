h, w = map(int, input().split())

ss = []

for i in range(h):
    ss.append(input())

count = 0

# horizontal
for s in ss:
    for cell in range(0, len(s)-1):
        if s[cell] == "." and s[cell+1] == ".":
            count += 1

# vertical
for i in range(w):
    for j in range(h-1):
        if ss[j][i] == "." and ss[j+1][i] == ".":
            count += 1

print(count)