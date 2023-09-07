t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    fence = list(map(int, input().split()))
    if fence[0] != n:
        res.append('NO')
    else:
        result = True
        for i in range(1, n):
            if fence[fence[i]-1] < i+1:
                res.append('NO')
                result = False
                break
        if result:
            res.append('YES')

for i in res:
    print(i)









