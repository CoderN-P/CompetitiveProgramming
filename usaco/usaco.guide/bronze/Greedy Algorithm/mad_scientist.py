"""
ID: neel.pa1
LANG: PYTHON3
TASK: breedflip
"""

fin = open('breedflip.in', 'r')
fout = open('breedflip.out', 'w')
n = int(fin.readline())
a = fin.readline().strip()
b = fin.readline().strip()

res = 0

for i in range(0, n):
    if a[i] != b[i]:
        if i == 0:
            res += 1
        elif b[i-1] == a[i-1]:
            res += 1

print(res, file=fout)
