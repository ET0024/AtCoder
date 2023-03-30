from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 8)

@lru_cache()
def f(k):
    if k == 0:
        return 1
    else:
        return f(k//2) + f(k//3)
    return k

n = int(input())
print(f(n))
