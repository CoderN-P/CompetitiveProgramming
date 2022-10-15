"""
ID: neel.pa1
LANG: PYTHON3
TASK: pails
"""

file_in = open('pails.in', 'r')
file_out = open('pails.out', 'w')

x, y, m = list(map(int, file_in.readline().split()))
results = []

for a in range(1001):
    if a*x > m:
        break
    for b in range(1001):
        if b*y+a*x > m:
            break
        results.append(b*y+a*x)
file_out.write(str(max(results))+'\n')