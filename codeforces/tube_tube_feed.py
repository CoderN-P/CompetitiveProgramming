q = int(input())
res = []

for _ in range(0, q):
    n, t = list(map(int, input().split()))
    durations = list(map(int, input().split()))
    entertainment = list(map(int, input().split()))
    ans = sorted({i:entertainment[i] for i in range(0, n) if i+durations[i] <= t}.items(), key=lambda x:x[1])
    if ans:
        res.append(ans[-1][0]+1)
    else:
        res.append(-1)

for i in res:
    print(i)



