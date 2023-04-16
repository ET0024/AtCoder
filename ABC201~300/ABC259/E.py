from collections import defaultdict

n = int(input())
m = []
pe_pair = [defaultdict(int) for _ in range(n)]
all_p = set()
d = defaultdict(list)
for i in range(n):
    _m = int(input())
    m.append(_m)

    for _ in range(_m):
        _p, _e = map(int, input().split())
        pe_pair[i][_p] = _e

        all_p.add(_p)
        d[_p].append(_e)

all_p = sorted(list(all_p))

for key, val in d.items():
    d[key] = sorted(val, reverse=True)
    if len(d[key]) == 1:
        d[key].append(0)
    else:
        d[key] = d[key][:2]
#
# print('---')
# print("debug:d=", d)
# print(pe_pair)
# print(all_p)
# print('---')

possible_set = set()

for i in range(n):
    ans = ""
    # for key in all_p:
    #     tmp = pe_pair[i][key]
    #     if tmp > 0 and tmp == d[key][0] and d[key][1] > 0:
    #         ans += "," + str(key) + "-" + str(d[key][1])

    for key in all_p:
        if pe_pair[i][key] == 0:
            ans += str(d[key][0])
        elif pe_pair[i][key] != d[key][0]:
            ans += str(d[key][0])
        else:
            ans += str(d[key][1])

    possible_set.add(ans)

print(len(possible_set))
