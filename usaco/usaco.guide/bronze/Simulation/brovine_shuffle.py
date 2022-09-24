"""
ID: neel.pa1
LANG: PYTHON3
TASK: shuffle
"""

file_in = open("shuffle.in", "r")
file_out = open("shuffle.out", "w")

cow_amt = int(file_in.readline())
shuffle = list(map(int, file_in.readline().split()))
ids = list(file_in.readline().split())
original_order = [None for _ in range(cow_amt)]

for i, val in enumerate(shuffle, start=1):
    next_index = val
    for _ in range(2):
        next_index = shuffle[next_index-1]

    original_order[i-1] = ids[next_index-1]

file_out.write('\n'.join(original_order)+'\n')
