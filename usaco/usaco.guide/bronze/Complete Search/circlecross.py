"""
ID: neel.pa1
LANG: PYTHON3
TASK: circlecross
"""

fin = open('circlecross.in', 'r')
fout = open('circlecross.out', 'w')

s = list(fin.readline().strip())

res = 0

d = {}

for i in range(0, 52):
    letter = s[i]
    if letter not in d:
        d[letter] = [i]
    else:
        d[letter].append(i)

for i in range(0, 26):
    interval = d[chr(65+i)]
    for j in range(i+1, 26):
        interval2 = d[chr(65+j)]
        if interval[0] < interval2[0] < interval[1] < interval2[1]:
            res += 1
        elif interval2[0] < interval[0] < interval2[1] < interval[1]:
            res += 1

print(res, file=fout)



