t = int(input())
res = []

for _ in range(0, t):
    n, k = int(input())
    lo, hi = 0, n

    while hi > lo:
        mid = (hi+lo)//2

        