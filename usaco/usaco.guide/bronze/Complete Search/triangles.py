"""
ID: neel.pa1
LANG: PYTHON3
TASK: triangles
"""

fin = open('triangles.in', 'r')
fout = open('triangles.out', 'w')

n = int(fin.readline())
points = [list(map(int, fin.readline().split())) for _ in range(n)]


m = 0

for i in range(0, n):
    x, y = points[i]
    for j in range(0, n):
        if i == j:
            continue
        if x != points[j][0]:
            continue
        for k in range(0, n):
            if k == j:
                continue
            if y != points[k][1]:
                continue
            m = max(m, abs(points[j][0] - points[k][0]) * abs(points[i][1] - points[j][1]))

fout.write(str(m) + "\n")
