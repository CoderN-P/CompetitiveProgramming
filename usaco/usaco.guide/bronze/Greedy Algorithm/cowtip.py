"""
ID: neel.pa1
LANG: PYTHON3
TASK: cowtip
"""

fin = open('cowtip.in', 'r')
fout = open('cowtip.out', 'w')

n = int(fin.readline())
grid = [list(map(int, fin.readline().strip())) for _ in range(n)]

# find the farthest bottom left 1
res = 0

while True:
    m = 0
    v = None
    for row in range(0, n):
        for col in range(0, n):
            if grid[row][col] == 1:
                m = max(m, row+col)
                v = [row, col]
    if not v:
        break
    for row in range(0, v[0]+1):
        for col in range(0, v[1]+1):
            if grid[row][col] == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = 0

    res += 1

fout.write(str(res))


