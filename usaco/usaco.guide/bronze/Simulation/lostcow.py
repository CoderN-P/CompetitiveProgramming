"""
ID: neel.pa1
LANG: PYTHON3
TASK: lostcow
"""

file_in = open('lostcow.in', 'r')
file_out = open('lostcow.out', 'w')

x, y = list(map(int, file_in.readline().split()))
dist = 1
travelled = 0
coord = x

while True:
    endpoint = x+dist
    if (endpoint <= y and coord > y) or (endpoint >= y and coord < y):
        travelled += abs(coord - y)
        break
    else:
        travelled += abs(coord - endpoint)
        coord = endpoint
        dist *= -2


file_out.write(str(travelled)+'\n')