import math

x = int(input())

primes = [2]

for i in range(3, 10 ** 5 + 1000):
    is_prime = True
    target = math.sqrt(i) + 1

    for p in primes:
        if p > target:
            break
        if i % p == 0:
            is_prime = False
    if is_prime:
        primes.append(i)

for p in primes:
    if p >= x:
        print(p)
        exit()
