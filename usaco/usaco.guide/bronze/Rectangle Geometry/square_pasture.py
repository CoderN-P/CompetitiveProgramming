"""
ID: neel.pa1
LANG: PYTHON3
TASK: square
"""
file_in = open('square.in', 'r')
file_out = open('square.out', 'w')
a = list(map(int, file_in.readline().split()))
b = list(map(int, file_in.readline().split()))
result = max(max(a[2], b[2]) - min(a[0], b[0]), max(a[3], b[3]) - min(a[1], b[1]))**2
file_out.write(str(result)+'\n')
