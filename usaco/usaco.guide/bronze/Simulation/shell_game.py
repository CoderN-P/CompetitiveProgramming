"""
ID: neel.pa1
LANG: PYTHON3
TASK: shell
"""
file_in = open("shell.in", "r")
file_out = open("shell.out", "w")
swap_amt = int(file_in.readline())

shells = [0, False, False, False]
actual_swaps = []

for _ in range(0, swap_amt):
    actual_swaps.append(list(map(int, file_in.readline().split())))

points = [0, 0, 0]


for n in range(1, 4):
    shells[n] = True
    for swap in actual_swaps:
        shells[swap[0]], shells[swap[1]] = shells[swap[1]], shells[swap[0]]
        if shells[swap[2]]:
            points[n-1] += 1

    shells = [0, False, False, False]


file_out.write(str(max(points))+'\n')


