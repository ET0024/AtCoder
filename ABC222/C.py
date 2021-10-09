n, m = map(int, input().split())
hands = [list(input()) for _ in range(2 * n)]
score = [0 for _ in range(2 * n)]


def judge(hand1, hand2):
    if (hand1, hand2) in [('G', 'C'), ('C', 'P'), ('P', 'G')]:
        return 0
    elif (hand1, hand2) in [('C', 'G'), ('P', 'C'), ('G', 'P')]:
        return 1
    else:
        return -1


for round in range(m):
    score_sorted = [(-val, i) for i, val in enumerate(score)]
    score_sorted.sort(key=lambda x: (x[0], x[1]))

    for i in range(0, 2 * n, 2):
        _, player1 = score_sorted[i]
        _, player2 = score_sorted[i + 1]

        hand1 = hands[player1][round]
        hand2 = hands[player2][round]
        result = judge(hand1, hand2)
        if result == 0:
            score[player1] += 1
        elif result == 1:
            score[player2] += 1

score_sorted = [(-val, i) for i, val in enumerate(score)]
score_sorted.sort(key=lambda x: (x[0], x[1]))
for _, player in score_sorted:
    print(player + 1)
