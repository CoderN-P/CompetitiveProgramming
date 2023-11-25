t = int(input())

for _ in range(0, t):
    n, k, x = list(map(int, input().split()))
    if k > n or k > x+1:
        print(-1)
        continue
    mx = x if x != k else k-1
    s = (k-1) * k / 2

    s += (n-k)*mx
    print(int(s))



