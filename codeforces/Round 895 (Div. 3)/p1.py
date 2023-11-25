t = int(input())
res = []

for _ in range(0, t):
    a, b, c = list(map(int, input().split()))
    if a == b:
        res.append(0)
    else:
        diff = (max(a, b) - min(a, b))/2
        if c > diff:
            res.append(1)
        else:
            if diff%c == 0:
                res.append(int(diff//c))
            else:
                res.append(int(diff//c + 1))

for i in res:
    print(i)
