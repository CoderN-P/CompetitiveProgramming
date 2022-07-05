"""
ID: neel.pa1
LANG: PYTHON3
TASK: transform
"""

file_in = open("transform.in", "r")
file_out = open("transform.out", "w")

lines = int(file_in.readline())

pattern_before = []
pattern_after = []
for _ in range(0, lines):
    line = file_in.readline().strip()
    pattern_before.append([char for char in line])

for _ in range(0, lines):
    line = file_in.readline().strip()
    pattern_after.append([char for char in line])


def rotate(arr):
    return [list(reversed(s)) for s in list(zip(*arr))]


def reflect(arr):
    l = len(arr)
    new_arr = [[0 for _ in range(0, l)] for _ in range(0, l)]
    for i in range(0, l):
        for j in range(0, l):
            new_arr[i][j] = arr[i][l - 1 - j]

    return new_arr


result = 0

if rotate(pattern_before) == pattern_after:
    result = 1
elif rotate(rotate(pattern_before)) == pattern_after:
    result = 2
elif rotate(rotate(rotate(pattern_before))) == pattern_after:
    result = 3
elif reflect(pattern_before) == pattern_after:
    result = 4
elif rotate(reflect(pattern_before)) == pattern_after:
    result = 5
elif rotate(rotate(reflect(pattern_before))) == pattern_after:
    result = 5
elif rotate(rotate(rotate(reflect(pattern_before)))) == pattern_after:
    result = 5
elif pattern_before == pattern_after:
    result = 6
else:
    result = 7

file_out.write(str(result)+'\n')
