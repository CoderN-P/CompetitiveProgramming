t = int(input())
res = []

for _ in range(0, t):
    m = []

    for _ in range(0, 8):
        m.append(list(input()))

    ans = ''
    f = False
    for i in range(0, 8):
        if f:
            break
        for j in range(0, 8):
            if m[i][j] != '.':
                ans += m[i][j]
                r = i
                while r <= 6:
                    r += 1
                    if m[r][j] == '.':
                        break
                    else:
                        ans += m[r][j]
                f = True

    res.append(ans)

for i in res:
    print(i)





