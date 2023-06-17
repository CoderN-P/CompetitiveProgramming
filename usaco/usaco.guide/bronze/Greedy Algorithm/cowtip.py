"""
ID: neel.pa1
LANG: PYTHON3
TASK: cowtip
"""

fin = open('cowtip.in', 'r')
fout = open('cowtip.out', 'w')

n = int(fin.readline())
grid = [list(map(int, fin.readline().strip())) for _ in range(n)]

res = 0

