arr = [input().split() for _ in range(0, 5)]
idx = (0, 0)
for i in range(0, 5):
    for j in range(0, 5):
        if arr[i][j] == '1':
            idx = (i, j)

print(abs(idx[0]-2)+abs(idx[1]-2))
