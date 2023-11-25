t = int(input())

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans1 = 0
    ans2 = 0
    b1 = min(b)
    a1 = min(a)
    for i in range(0, n):
        ans1 += b1+a[i]
        ans2 += a1+b[i]

    print(min(ans1, ans2))