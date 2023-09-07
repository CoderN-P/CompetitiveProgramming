t = int(input())
res = []
for _ in range(0, t):
    n = int(input())
    ans = [0, 0]
    for i in range(1, n+1):
        a, b = list(map(int, input().split()))

        if a <= 10:
            if b > ans[1]:
                ans = [i, b]
    res.append(ans)

for i in res:
    print(i[0])


