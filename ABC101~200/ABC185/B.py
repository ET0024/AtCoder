N, M, T = map(int, input().split())

current_power = N
prev_time = 0

for _ in range(M):
    a, b = map(int, input().split())

    # battery on enter time
    current_power -= (a - prev_time)
    if current_power <= 0:
        print("No")
        exit()

    # charge in cafe
    current_power = min(current_power + (b - a), N)
    prev_time = b

current_power -= (T - prev_time)
if current_power <= 0:
    print("No")
    exit()

print("Yes")
