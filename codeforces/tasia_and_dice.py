t = int(input())
res = []

for _ in range(0, t):
    n, s, r = list(map(int, input().split()))
    result = [0 for _ in range(0, n)]
    result[-1] = s-r
    mod = r%(n-1)
    v = r//(n-1)
    for i in range(0, n-1):
        if mod > 0:
            result[i] = v + 1
        else:
            result[i] = v
        mod -= 1

    res.append(' '.join(list(map(str, result))))
for i in res:
    print(i)