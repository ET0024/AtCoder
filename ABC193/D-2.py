from collections import defaultdict

k = int(input())
s = input()
t = input()

cards_s = defaultdict(int)
cards_t = defaultdict(int)

for i in range(4):
    cards_s[int(s[i])] += 1
    cards_t[int(t[i])] += 1

count = 0
for s_last in range(1, 10):
    for t_last in range(1, 10):
        # 組み合わせが有り得るかをチェック
        if s_last == t_last:
            if cards_s[s_last] + cards_t[s_last] + 2 > k:
                continue
        else:
            if cards_s[s_last] + cards_t[s_last] + 1 > k:
                continue
            if cards_s[t_last] + cards_t[t_last] + 1 > k:
                continue

        score_s = 0
        score_t = 0
        cards_s[s_last] += 1
        cards_t[t_last] += 1
        for i in range(1, 10):
            score_s += i * 10 ** (cards_s[i])
            score_t += i * 10 ** (cards_t[i])
        cards_s[s_last] -= 1
        cards_t[t_last] -= 1

        if score_s > score_t:
            if s_last == t_last:
                rem_cards = k - cards_s[s_last] - cards_t[t_last]
                if rem_cards > 1:
                    count += rem_cards * (rem_cards - 1)
            else:
                count += (k - cards_s[s_last] - cards_t[s_last]) \
                         * (k - cards_s[t_last] - cards_t[t_last])

total_case = (9 * k - 8) * (9 * k - 9)
print(count / total_case)
