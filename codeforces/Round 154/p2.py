t = int(input())
res = []

for _ in range(0, t):
    a1 = list(input())
    a2 = list(input())
    between = False
    start = ''
    for n, v in enumerate(zip(a1, a2)):
        a, b = v
        if n < len(a1) - 1:
            if a != a1[n + 1]:
                between = True
                start = a

        if a != b:
            if not between:
                res.append('NO')
                start = False
                break
    if start is not False:
        res.append('YES')


for i in res:
    print(i)
