import math

n = int(input())

a_max = int(math.log(n) / math.log(3)) + 1
b_max = int(math.log(n) / math.log(5)) + 1

a_ans = -1
b_ans = -1

for a in range(1, a_max+1):
    for b in range(1, b_max+1):
    # for b in range(1, int(math.log(n - 3 ** a + 1) / math.log(5))):

        if 3 ** a + 5 ** b - n == 0:
            a_ans = a
            b_ans = b
            break

if a_ans == -1:
    print(-1)
else:
    print(a_ans, b_ans)
