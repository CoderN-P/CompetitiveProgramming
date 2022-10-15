"""
ID: neel.pa1
LANG: PYTHON3
TASK: milk3
"""

file_in = open('milk3.in', 'r')
file_out = open('milk3.out', 'w')

A, B, C = list(map(int, file_in.readline().split()))

initial = (0, 0, C)
results = []
visited = [[[None for z in range(21)] for y in range(21)] for x in range(21)]


def search(a, b, c):
    print(a, b, c)
    if visited[a][b][c]: return
    visited[a][b][c] = True
    if a == 0: results.append(c)

    x = min(a, B-b)
    search(a - x, b + x, c)
    x = min(b, A-a)
    search(a + x, b - x, c)
    x = min(a, C-c)
    search(a - x, b, c + x)
    x = min(c, A-a)
    search(a + x, b, c - x)
    x = min(b, C-c)
    search(a, b - x, c + x)
    x = min(c, B-b)
    search(a, b + x, c - x)


search(*initial)
file_out.write(" ".join(list(map(str, sorted(results))))+'\n')
