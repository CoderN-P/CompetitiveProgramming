"""
ID: neel.pa1
LANG: PYTHON3
TASK: gymnastics
"""

fin = open('gymnastics.in', 'r')
fout = open('gymnastics.out', 'w')

k, n = map(int, fin.readline().split())
sessions = [list(map(int, fin.readline().split())) for _ in range(k)]

count = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        for session in sessions:
            if session.index(i) < session.index(j):
                break
        else:
            count += 1

print(count, file=fout)

