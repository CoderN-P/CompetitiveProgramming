"""
ID: neel.pa1
LANG: PYTHON3
TASK: mixmilk
"""

file_in = open("mixmilk.in", "r")
file_out = open("mixmilk.out", "w")

buckets = [list(map(int, line.strip().split())) for line in file_in.readlines()]

for n in range(0, 10):

    from_index = n % len(buckets)
    to_index = from_index+1
    if from_index == len(buckets)-1:
        to_index = 0

    milk_sum = buckets[from_index][1] + buckets[to_index][1]
    leftover_sum = 0
    if milk_sum > buckets[to_index][0]:
        leftover_sum = milk_sum - buckets[to_index][0]
        milk_sum = buckets[to_index][0]

    buckets[from_index][1] = leftover_sum
    buckets[to_index][1] = milk_sum


file_out.write('\n'.join([str(b[1]) for b in buckets]))

