t = int(input())
res = []

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    mice = sorted(list(map(int, input().split())), reverse=True)

    lo, hi = 0, k
    while hi > lo:
        mid = (lo+hi)//2
        # determine if [mid] mice can be saved
        v = sum([n-mice[i] for i in range(0, mid+1)])

        if v >= n:
            hi = mid
        else:
            lo = mid+1

    res.append(lo)

for i in res:
    print(i)
