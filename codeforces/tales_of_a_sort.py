t = int(input())

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0

    for i in range(1, n):
        if a[i] < a[i-1]:
            c = max(c, a[i-1])
    print(c)
