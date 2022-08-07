n = int(input())

prev = []
a = []

for i in range(n):
    # prevにaの参照を渡してaは初期化
    prev = a
    a = []
    for j in range(i + 1):
        if j == 0 or j == i:
            a.append(1)
        else:
            a.append(prev[j - 1] + prev[j])
    print(*a)
