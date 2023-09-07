t = int(input())

res = []


for _ in range(0, t):
    n, k = list(map(int, input().split()))
    l = sorted(list(map(int, input().split())))
    s = 0
    cur = 0
    for i in range(1, n):
        if l[i] - l[i-1] <= k:

            cur += 1
            if i == n - 1:
                s = max(s, cur)
        else:
            s = max(s, cur)
            cur = 0

    res.append(n-s-1)

for i in res:
    print(i)



