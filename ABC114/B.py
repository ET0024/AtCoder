S = input()

diff = float('inf')

for i in range(len(S) - 2):
    a = int(S[i]) * 100 + int(S[i + 1]) * 10 + int(S[i + 2])
    if abs(753 - a) < diff:
        diff = abs(753 - a)

print(diff)