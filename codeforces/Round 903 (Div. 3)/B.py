t = int(input())

for _ in range(t):
    a, b, c = list(map(int, input().split()))

    s = sorted([a, b, c])

    s.append(s[2]-s[0])
    s[2] = s[0]

    s.append(s[1]-s[0])

    s[1] = s[0]



    ops = 3 - 2 + s.count(0)



    if s[-1] != s[0] and s[-1] and s[-1] != 0:
        if s[-1] == s[0]*2:
            s[-1] = s[0]
            ops -= 1
        elif s[-1] == s[0]*3:
            if ops < 2:
                print('NO')
                continue
            else:
                ops = 0
                s[-1] = s[0]
        else:
            print('NO')
            continue

    if s[-2] != s[0] and s[-2] and s[-2] != 0:
        if s[-2] == s[0]*2:
            if ops < 1:
                print('NO')
                continue
            s[-2] = s[0]
            ops -= 1

        elif s[-2] == s[0]*3:
            if ops < 2:
                print('NO')
                continue
            else:
                ops = 0
                s[-1] = s[0]

        else:
            print('NO')
            continue

    print('YES')





