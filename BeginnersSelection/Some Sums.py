n, a, b = map(int, input().split())
count = 0

for i in range(1, n+1):
    digit_1 = int((i % 10))
    digit_2 = int(((i % 100) - digit_1) / 10)
    digit_3 = int(((i % 1000) - 10 * digit_2 - digit_1) / 100)
    digit_4 = int(((i % 10000) - 100 * digit_3 - 10 * digit_2 - digit_1) / 1000)
    digit_5 = int(((i % 100000) - 1000 * digit_4 - 100 * digit_3 - 10 * digit_2 - digit_1) / 10000)
    digit_sum = digit_1 + digit_2+digit_3+digit_4+digit_5

    if a <= digit_sum & digit_sum <= b:
        count += i

print(count)