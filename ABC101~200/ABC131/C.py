import math

a, b, c, d = map(int, input().split())
lcm = c * d // math.gcd(c, d)


def num_div(divisor):
    return (b // divisor) - ((a - 1) // divisor)


print((b - a + 1) - num_div(c) - num_div(d) + num_div(lcm))
