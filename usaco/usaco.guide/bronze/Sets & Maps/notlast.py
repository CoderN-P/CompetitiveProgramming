"""
ID: neel.pa1
LANG: PYTHON3
TASK: notlast
"""

fin = open("notlast.in", "r")
fout = open("notlast.out", "w")

n = int(fin.readline())
d = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}


for _ in range(0, n):
    name, p = fin.readline().split()
    p = int(p)
    d[name] += p


second_last = ""
d = dict(sorted(list(d.items()), key=lambda x: x[1]))

index = None
v = 0
m = 0
for i, x in enumerate(d.items()):
    if i == 0:
        m = x[1]
    if index:
        if x[1] == v:
            second_last = ""
        break
    if x[1] != m:
        v = x[1]
        second_last = x[0]
        index = i


if second_last == "":
    print('Tie', file=fout)
else:
    print(second_last, file = fout)

