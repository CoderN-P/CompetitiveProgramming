t = int(input())

for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(0, n):
        prod = 1
        for j in range(0, n):
            if j == i:
                prod *= arr[i]+1
            else:
                prod*= arr[j]
        ans = max(ans, prod)
    print(ans)

