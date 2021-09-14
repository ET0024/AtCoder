import math

a, b, h, m = map(int, input().split())

PI = math.pi

theta_a = 2 * PI * (h / 12 + m / 60 / 12)
theta_b = 2 * PI * (m / 60)

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta_a - theta_b)))
