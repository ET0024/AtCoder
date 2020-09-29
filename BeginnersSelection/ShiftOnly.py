def is_all_even(lst):
    for value in lst:
        if value % 2 != 0:
            return False

    return True


def divide_by_half_value(lst):
    return list(map(lambda x: int(x / 2), lst))


n = int(input())
a = list(map(int, input().split()))

count = 0

while True:
    if is_all_even(a):
        count += 1
        a = divide_by_half_value(a)
    else:
        break

print(count)
