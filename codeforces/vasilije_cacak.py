t = int(input())

for _ in range(0, t):
    n, k, x = list(map(int, input().split()))

    if k*(k+1)/2 <= x <= n*(n+1)/2 - (n-k)*(n-k+1)/2:
        print('YES')
    else:
        print('NO')