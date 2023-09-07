"""
ID: neel.pa1
LANG: PYTHON3
TASK: crosswords
"""

fin = open('crosswords.in', 'r')
fout = open('crosswords.out', 'w')


n, m = list(map(int, fin.readline().split()))

grid = [list(fin.readline()) for _ in range(0, n)]

count = 0
indeces = []
for i in range(0, n):
    for j in range(0, m):
        cell = grid[i][j]
        h = False
        if cell == '.':
            if (j == 0 or grid[i][j-1] == '#') and j < n-2:
                if grid[i][j+1] == '.' and grid[i][j+2] == '.':
                    count += 1
                    h = True
                    indeces.append((i, j))

            if (i == 0 or grid[i-1][j] == '#') and i < m-2:
                if grid[i+1][j] == '.' and grid[i+2][j] == '.':
                    if not h:
                        count += 1
                        indeces.append((i, j))

print(count, file=fout)

for idx in indeces:
    print(idx[0]+1, idx[1]+1, file=fout)


