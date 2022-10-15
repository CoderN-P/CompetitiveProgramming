"""
ID: neel.pa1
LANG: PYTHON3
TASK: skidesign
"""


file_in = open('skidesign.in', 'r')
file_out = open('skidesign.out', 'w')

hills = int(file_in.readline())
sorted_elevations = [int(file_in.readline().strip()) for _ in range(hills)]
results = []

for i in range(1, 84):

    if i+17 > max(sorted_elevations): break
    r = 0
    for j in sorted_elevations:
        x = 0
        if j < i:
            x = (i-j)**2
        elif j > i+17:
            x = (j-(i+17))**2
        r += x
    results.append(r)

result = min(results)


file_out.write(str(result)+'\n')
