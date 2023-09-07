t = int(input())
res = []

for _ in range(0, t):
    n, u, v  = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = float('inf')
    constant = 10**6
    diffprev = 0
    for row, col in enumerate(a):
        if row == 0:
            continue
        else:
            diff = abs(a[row-1] - col)
            if diff > 1:
                ans = 0
                break
            else:
                if diff == 0:
                    ans = min(ans, min(v+v, u+v))
                    if diffprev == 1:
                        ans = min(ans, u+u)
                else:
                    if row == 1 and col == 0:
                        ans = u*2
                    else:
                        ans = min(ans, min(u, v))
            diffprev = diff
    res.append(ans)

for i in res:
    print(i)

