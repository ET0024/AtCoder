# binary search version
import math


def can_split(m, n):
    if m * (m + 1) <= 2 * (n + 1):
        return True
    else:
        return False


def binary_search(n, low, high, is_ok):
    if not is_ok(low) or is_ok(high):
        print("initial value error")
        return None

    while high - low > 1:
        mid = int((high + low) / 2)
        if is_ok(mid):
            low = mid
        else:
            high = mid

    return low


n = int(input())
m = binary_search(n, 0, 2 * (n + 1), lambda x: can_split(x, n))

print(n - m + 1)
