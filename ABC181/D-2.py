from collections import Counter

S = list(map(int, list(input())))
cnt = Counter(S)

candidate_cnt = []

if len(S) == 1:
    if int(S[0]) % 8 == 0:
        print("Yes")
        exit()

if len(S) == 2:
    if int(10 * S[0] + S[1]) % 8 == 0 or int(10 * S[1] + S[0]) % 8 == 0:
        print("Yes")
        exit()

for i in range(100, 1000):
    if i % 8 == 0:
        candidate_cnt.append(Counter(list(map(int, list(str(i))))))

for candidate in candidate_cnt:

    satisfied = True
    for key in candidate:

        if candidate[key] > cnt[key]:
            satisfied = False

    if satisfied:
        print("Yes")
        exit()

print("No")
