t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    if n%2 == 1:
        if n == 1:
            res.append('1')
        else:
            res.append('-1')
    else:
        ans = [n, n-1]
        ans += list(range(2, n-1))
        if 1 not in ans:
            ans.append(1)
        res.append(' '.join(map(str, ans)))
for i in res:
    print(i)