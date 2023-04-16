n, x = map(int, input().split())
a = list(map(int, input().split()))

nokori = (x, 0)
otsuri = (x, 0)

for i in range(n-1, -1, -1):
    nokori_val = nokori[0]
    nokori_count = nokori[1]
    otsuri_val = otsuri[0]
    otsuri_count = otsuri[1]

    
    min(nokori_count + nokori_val % a[i], otsuri_count + otsuri_val % a[i])


    for val , count in possible:
        # 少な目に払う

        print(val)
        print(count)
    # print(a[i])