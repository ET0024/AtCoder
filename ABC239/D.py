is_prime = [True for _ in range(201)]
is_prime[0] = False
is_prime[1] = False
for div in range(2, 201):
    if not is_prime[div]:
        continue
    for i in range(2, 201):
        if div * i > 200:
            continue
        is_prime[div * i] = False

primes = set()
for i, b in enumerate(is_prime):
    if b:
        primes.add(i)

a, b, c, d = map(int, input().split())

for takahashi_val in range(a, b + 1):
    aoki_set = set([x + takahashi_val for x in range(c, d + 1)])
    if len(aoki_set.intersection(primes))==0:
        print('Takahashi')
        exit()
print('Aoki')
