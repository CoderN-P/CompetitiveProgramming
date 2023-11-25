t = int(input())

for _ in range(0, t):
    n, x = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))

    lo, hi = 0, 2*10**9

    while lo < hi:
        mid = lo + (hi-lo+1)//2
        used = 0
        for i in range(0, n):
            if a[i] >= mid:
                break
            else:
                used += mid - a[i]
        if used > x:
            hi = mid-1
        else:
            lo = mid
    print(lo)

