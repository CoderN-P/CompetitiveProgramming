"""
ID: neel.pa1
LANG: PYTHON3
TASK: lostcow
"""
fin = open('lostcow.in', 'r')
fout = open('lostcow.out', 'w')


x, y = list(map(int, fin.readline().split()))
res = 0
pos = x
inc = 1

while True:
    if (pos > y >= x + inc) or (pos < y <= x + inc):
        res += abs(pos-y)
        break

    res += abs(pos - x - inc)
    pos = x + inc
    inc *= -2
    
print(res, file=fout)