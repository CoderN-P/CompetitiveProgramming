"""
ID: neel.pa1
LANG: PYTHON3
TASK: cowjog
"""

fin = open('cowjog.in', 'r')
fout = open('cowjog.out', 'w')

n = int(fin.readline())
c = [list(map(int, fin.readline().split())) for _ in range(0, n)]
m = sorted(c, key=lambda x: x[0])[-1][0]
c = dict(c)


cows = []

for i in range(0, m+1):
    if i in c:
        cows.append(c[i])
    else:
        cows.append(0)


count = 1
start = cows[0]
for i in range(1,m+1):
    if cows[i] == 0 and cows[i-1] != 0:
        start = 0
    if (cows[i] < start and cows[i] != 0) or (cows[i-1] == 0 and cows[i] != 0):
        start = cows[i]
        count += 1

print(count, file=fout)