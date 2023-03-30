'''
なぜ転倒数がバブルソートの交換回数と一致するのか？
・bubble sortの交換1回につき大小関係の逆転が1つ解消する＝転倒数は1減少する
・バブルソートが完了した時点で転倒数は0になる
ことから、バブルソートの交換回数は初期状態の転倒数に一致する
（この観察からすると、ソート対象に同じ数字が含まれていても同じ論理が成り立つ）
'''
from collections import defaultdict

s = input()
n = len(s)
d = defaultdict(int)
for i, c in enumerate(list('atcoder')):
    d[c] = i

s2 = [d[s[i]] for i in range(n)]

# calc inversion no
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if s2[i] > s2[j]:
            count += 1

print(count)
