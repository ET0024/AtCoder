from collections import Counter

S_str = input()
S = list(map(int, list(S_str)))
cnt = Counter(S)
N = len(S)

possible_list = []

for i in range(100, 1000):
    if i % 8 == 0:
        a = i // 100
        b = (i - 100 * a) // 10
        c = (i - 100 * a - 10 * b)
        possible_list.append(Counter([a, b, c]))

is_exist = False

if N == 1:
    if S[0] % 8 == 0:
        is_exist = True

if N == 2:
    if (10 * S[0] + S[1]) % 8 == 0 or (10 * S[1] + S[0]) % 8 == 0:
        is_exist = True

if N >= 3:
    for sample in possible_list:

        check_local = True

        for k in sample:
            check_local *= (cnt[k] >= sample[k])

        if check_local:
            is_exist = True

if is_exist:
    print("Yes")
else:
    print("No")
