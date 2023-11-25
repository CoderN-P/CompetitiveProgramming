t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    ds = [list(map(int, input().split())) for _ in range(0, n)]
    2x - ds[0] = ds[1]
    for en, i in enumerate(ds):
        v = ds[en]
        s = v[0] + v[1]
        if s%2 == 0:
            ds[en] = s/2
        else:
            ds[en] = s//2 + 1

    ds = sorted(reverse)



