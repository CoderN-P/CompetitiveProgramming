t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    nums = list(range(1, n+1))
    a = sorted([[a[i], i] for i in range(0, n)], key=lambda x: x[0], reverse=True)
    for i in range(0, n):
        a[i].append(nums[i])
    result = [0 for _ in range(0, n)]
    for i in range(0, n):
        v = a[i]
        result[v[1]] = v[2]
    res.append(' '.join(list(map(str, result))))

for i in res:
    print(i)
