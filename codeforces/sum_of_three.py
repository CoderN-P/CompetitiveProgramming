t = int(input())

for _ in range(0, t):
    n = int(input())

    v = n//3
    m = n%3

    if v == 1:
        print('NO')
    else:
        v1 = 0
        v2 = 0
        v3 = 0
        if v%3 == 0:
            print('NO')
            continue
        if (v-1)%3 == 0:
            v1 = v-2
            v2 += 1
        if (v+1+m)%3 == 0:

        print(v1, 2, v+1+m)