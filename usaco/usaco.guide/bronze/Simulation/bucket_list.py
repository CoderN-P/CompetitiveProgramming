"""
ID: neel.pa1
LANG: PYTHON3
TASK: blist
"""

fin = open("blist.in", "r")
fout = open("blist.out", "w")

n = int(fin.readline())
events = sorted([list(map(int, fin.readline().split())) for _ in range(0, n)], key=lambda x: x[0])

mtime = events[-1][1]
used = 0
for i in range(0, 1001):
    tmp = 0
    for event in events:
        if event[0] <= i <= event[1]:
            tmp += event[2]

    used = max(tmp, used)

print(used, file=fout)











