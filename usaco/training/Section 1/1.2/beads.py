"""
ID: neel.pa1
LANG: PYTHON3
TASK: beads
"""

file_in = open("beads.in", "r")
file_out = open("beads.out", "w")

# created 2 arrays to store occurences of bead colors to the left and to the right of a certain index
size = 2 * int(file_in.readline().strip())
chars = file_in.readline().strip() * 2
right = [[0, 0] for _ in range(0, size + 1)]
left = [[0, 0] for _ in range(0, size + 1)]


for i in range(1, size):
    if chars[i - 1] == "r":
        left[i][0] = left[i - 1][0] + 1
        left[i][1] = 0
    elif chars[i - 1] == "b":
        left[i][1] = left[i - 1][1] + 1
        left[i][0] = 0
    else:
        left[i][0] = left[i - 1][0] + 1
        left[i][1] = left[i - 1][1] + 1


for i in range(size - 1, -1, -1):
    if chars[i] == "r":
        right[i][0] = right[i + 1][0] + 1
        right[i][1] = 0
    elif chars[i] == "b":
        right[i][1] = right[i + 1][1] + 1
        right[i][0] = 0
    else:
        right[i][0] = right[i + 1][0] + 1
        right[i][1] = right[i + 1][1] + 1

max_beads = 0

for i in range(0, size):
    max_beads = max(
        max_beads, max(left[i][1], left[i][0]) + max(right[i][1], right[i][0])
    )
if max_beads > size // 2:
    max_beads = size // 2
file_out.write(str(max_beads) + "\n")
