t = int(input())
res = []

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    if k < n:
        if (n - k) <= k:
            k = k+k
        else:
            if n%k == 0:
                k = n
            else:
                k = ((n//k)+1)*k
    result = k//n

    if k%n != 0:
        result += 1
    res.append(result)

for i in res:
    print(i)
