t = int(input())

res = []


for _ in range(0, t):
    n = int(input())
    ans = ''

    for i in range(1, n+1, 2):
        cur = i
        while cur <= n:
            ans += f' {str(cur)}'

            cur *= 2

    res.append(ans)

for i in res:
    print(i)

