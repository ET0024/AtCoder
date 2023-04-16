n, x = map(int, input().split())

alph = [chr(i) for i in range(97, 123)]
s = []
for i in range(26):
    for _ in range(n):
        s.append(alph[i])

print(s[x-1].upper())
