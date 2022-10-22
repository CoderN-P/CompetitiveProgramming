"""
ID: neel.pa1
LANG: PYTHON3
TASK: ariprog
"""

import re




file_in = open('ariprog.in', 'r')
file_out = open("ariprog.out", "w")
n = int(file_in.readline())
m = int(file_in.readline())
bss = [False]*(2*m*m+1)

print(bytes(f'1(?:.{{{4}}}1){{{5}}}'.encode('utf8')))

for i in range(0, m+1):
    for j in range(i, m+1):
        bss[i**2+j**2] = True
limit = 2*m*m

results = []
for width in range(1, len(bss)//(n-1)+1):
    for start in range(0, len(bss)-(width*(n-1))):
        mx = start+(width*n)
        if all(bss[start:mx:width]):
            results.append(f'{start} {width}')
if not results:
    file_out.write('NONE\n')
else:
    file_out.write('\n'.join(results)+'\n')


