n = int(input())
arr = [list(map(int, input().split())) for _ in range(0, n)]
res = 'YES'
for j in range(0,  3):
    s = 0
    for i in range(0, n):
        s += arr[i][j]

    if s != 0:
        res = 'NO'
print(res)
