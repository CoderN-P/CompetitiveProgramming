t = int(input())




for _ in range(0, t):
    n, k, q = list(map(int, input().split()))

    temp = list(map(int, input().split()))

    ans = 0
    cur = 0
    for i in range(0, n):
        if temp[i] <= q:
            cur += 1
        else:
            if cur >= k:
                ans += (cur-k+1)*(cur-k+2)//2
            cur = 0

    if cur >= k:
        ans += (cur-k+1)*(cur-k+2)//2

    print(ans)
