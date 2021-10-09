k = int(input())
a, b = input().split()
a2, b2 = 0, 0
for i, digit in enumerate(reversed(a)):
    a2 += int(digit) * k ** i
for i, digit in enumerate(reversed(b)):
    b2 += int(digit) * k ** i

print(a2 * b2)
