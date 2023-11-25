t = int(input())

for _ in range(0, t):
    n = int(input())
    res = []

    for i in range(1, 2*n, 2):
        res.append(i)

    print(' '.join(list(map(str, res))))
