"""
ID: neel.pa1
LANG: PYTHON3
TASK: skidesign
"""


file_in = open('skidesign.in', 'r')
file_out = open('skidesign.out', 'w')

hills = int(file_in.readline())
sorted_elevations = [int(file_in.readline().strip()) for _ in range(0, hills)]

result = 0

while max(sorted_elevations) - min(sorted_elevations) - 17 > 0:
    sorted_elevations1 = sorted(sorted_elevations)
    lowest, highest, second_highest = sorted_elevations1[0], sorted_elevations[-1], sorted_elevations[-2]
    diff = highest - lowest - 17
    p1 = diff // 2
    p2 = diff - p1
    result += p1**2 + p2**2

    sorted_elevations[sorted_elevations.index(highest)] = p1
    sorted_elevations[sorted_elevations.index(lowest)] = p2

file_out.write(str(result)+'\n')
