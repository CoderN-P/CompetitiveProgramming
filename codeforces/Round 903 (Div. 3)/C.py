
t = int(input())

for _ in range(0, t):
    n = int(input())
    grid = [list(input()) for _ in range(0, n)]
    d = {}

    c = 0

    for i in range(0, n):
        for j in range(0, n):

            if grid[i][j] != grid[j][n-i-1] and grid[i][j] != 'z':
                v = abs(ord(grid[i][j]) - ord(grid[i][n - i - 1]))

                grid[i][j] = grid[j][n - i - 1]
                if grid[i][j] not in d:
                    d[grid[i][j]] = [grid[j][n-i-1]]
                    c += v
                else:
                    if grid[j][n-i-1] in d[grid[i][j]]:


    print(c)
