import math
t = int(input())

res = []

for _ in range(0, t):
    x, y, n = list(map(int, input().split()))
    arr = [0 for _ in range(0, n)]
    arr[0] = x
    arr[-1] = y
    nums = n - 2
    diff = y - x
    x = (diff - (nums * (nums + 1)) / 2) / (nums + 1)
    mod = math.ceil((x - x // 1) * (nums + 1))
    if x//1 == 0:
        res.append(-1)
    else:
        diffs = [x + i for i in range(nums, -1, -1)]
        diffs[0] += mod
        for i in range(1, n - 1):
            arr[i] = int(arr[i - 1] + diffs[i - 1])
        res.append(arr)

for i in res:
    if i == -1:
        print(i)
    else:
        print(' '.join(map(str, i)))
