"""
ID: neel.pa1
LANG: PYTHON3
TASK: cownomics
"""

fin = open('cownomics.in', 'r')
fout = open('cownomics.out', 'w')

n, m = map(int, fin.readline().split())
s = [fin.readline().strip() for _ in range(n)]
c = [fin.readline().strip() for _ in range(n)]

spotty = []
clean = []

for i in range(0, m):
    l = []
    for j in range(0, n):
        l.append(s[j][i])
    spotty.append(l)

for i in range(0, m):
    l = []
    for j in range(0, n):
        l.append(c[j][i])
    clean.append(l)

res = []

for i in range(0, m):
    if set(spotty[i]).isdisjoint(set(clean[i])):
        res.append(i)

print(len(res), file=fout)
