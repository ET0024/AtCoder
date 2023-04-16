def score(x):
    ans = 0
    for i in range(9):
        ans += (i + 1) * 10 ** x[i]
    return ans


k = int(input())
s = input()
t = input()

s = [s.count(str(i + 1)) for i in range(9)]
t = [t.count(str(i + 1)) for i in range(9)]
nokori = [k - s[i] - t[i] for i in range(9)]

s_win_case = 0
t_win_case = 0

for s_last in range(1, 10):
    for t_last in range(1, 10):
        s_added = s.copy()
        s_added[s_last - 1] += 1
        t_added = t.copy()
        t_added[t_last - 1] += 1

        nokori_added = [k - s[i] - t[i] for i in range(9)]
        if min(nokori_added) < 0:
            break

        tmp_s = nokori[s_last - 1] / sum(nokori)
        nokori2 = nokori.copy()
        nokori2[s_last - 1] -= 1
        tmp_t = nokori2[t_last - 1] / sum(nokori2)
        tmp = tmp_s * tmp_t
        if score(s_added) > score(t_added):
            s_win_case += tmp
        else:
            t_win_case += tmp

print(s_win_case / (s_win_case + t_win_case))
