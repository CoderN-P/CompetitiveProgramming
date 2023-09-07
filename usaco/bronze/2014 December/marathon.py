"""
ID: neel.pa1
LANG: PYTHON3
TASK: marathon
"""

fin = open('marathon.in', 'r')
fout = open('marathon.out', 'w')
n = int(fin.readline())

checkpoints = [list(map(int, fin.readline().split())) for _ in range(0, n)]

max_saved = 0
total = 0


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for i in range(1, n - 1):
    prev = checkpoints[i - 1]
    cur = checkpoints[i]
    next = checkpoints[i + 1]
    v = distance(cur, prev)
    normal = v + distance(next, cur)
    short = distance(next, prev)
    max_saved = max(max_saved, normal-short)
    total += v

total += distance(checkpoints[-1], checkpoints[-2])
print(total-max_saved, file=fout)
