t = int(input())

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    lo, hi = 1, max(a) + k

    while lo < hi:
        mid = (lo+hi)//2
        for i in range(0, n):

