def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    missing = list(set(range(0, n+1)) - set(a))
    if len(missing) == 0:
        missing = n+1


    while k > 0:
        k -= 1
        for i in range(0, n):

