t = int(input())

res = []

for _ in range(0, t):
    n, m = list(map(int, input().split()))

    arr = []

    for i in range(0, n):
        arr.append(list(input()))

    arr = list(map(list, zip(*arr)))

    def solve():
        ans = 'NO'
        for i in range(0, m-3):
            for j in range(i+1, m-2):
                for k in range(j+1, m-1):
                    for f in range(k+1, m):
                        if 'v' in arr[i] and 'i' in arr[j] and 'k' in arr[k] and 'a' in arr[f]:
                            ans = 'YES'
                            return ans
        return ans

    res.append(solve())


for i in res:
    print(i)

