"""
ID: neel.pa1
LANG: PYTHON3
TASK: barn1
"""
from itertools import product

file_in = open("barn1.in", "r")
file_out = open("barn1.out", "w")

board_amount, stall_amount, cow_amount = list(map(int, file_in.readline().split()))

blocked_stalls = cow_amount
boards_used = cow_amount
cow_stalls = []

for _ in range(0, cow_amount):
    stall = int(file_in.readline())
    cow_stalls.append([stall, stall])


def test(nums):
    s = sorted(nums)
    return min([[a, b] for a, b in zip(s, s[1:])], key=lambda x: x[1][0] - x[0][1])

while boards_used > board_amount:
    to_combine = test(cow_stalls)
    blocked_stalls += to_combine[1][0] - to_combine[0][1] - 1
    boards_used -= 1
    cow_stalls[cow_stalls.index(to_combine[0])][1] = to_combine[1][1]
    del cow_stalls[cow_stalls.index(to_combine[1])]

file_out.write(str(blocked_stalls)+'\n')