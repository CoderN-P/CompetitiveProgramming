t = int(input())
res = []


for _ in range(0, t):
    n, m, k, H = list(map(int, input().split()))
    h_diff = [abs(H-i) for i in list(map(int, input().split()))]
    ans = 0
    for i in h_diff:
        if i%k == 0 and i <= m*k-k and i>0:
            ans += 1

    res.append(ans)

for i in res:
    print(i)

