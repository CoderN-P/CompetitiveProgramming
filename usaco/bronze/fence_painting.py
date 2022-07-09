"""
ID: neel.pa1
LANG: PYTHON3
TASK: paint
"""
file_in = open('paint.in', 'r')
file_out = open('paint.out', 'w')
l = list(map(int, file_in.readline().split()))
l2 = list(map(int, file_in.readline().split()))
total = (l[1] - l[0]) + (l2[1] - l2[0])
inter = max(0, min(l[1], l2[1]) - max(l[0], l2[0]))
file_out.write(str(total-inter)+'\n')