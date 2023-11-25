t = int(input())

for _ in range(0, t):
    grid = [input() for _ in range(0, 10)]

    pts = 0

    for i in range(0, 10):
        for j in range(0, 10):
            if grid[i][j] == 'X':
                if i in [0, 9] or j in  [0, 9]:
                    pts += 1
                elif i in [1, 8] or j in [1, 8]:
                    pts += 2
                elif i in [2, 7] or j in [2, 7]:
                    pts += 3
                elif i in [3, 6] or j in [3, 6]:
                    pts += 4
                elif i in [4, 5] or j in [4, 5]:
                    pts += 5
    print(pts)