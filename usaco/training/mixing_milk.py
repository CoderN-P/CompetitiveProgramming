"""
ID: neel.pa1
LANG: PYTHON3
TASK: milk
"""

file_in = open("milk.in", "r")
file_out = open("milk.out", "w")
milk_amt, farmer_amt = list(map(int, file_in.readline().split()))
farmers = sorted([list(map(int, file_in.readline().split())) for _ in range(0, farmer_amt)], key=lambda x: x[0])
cost = 0

for n in range(0, milk_amt):
    if farmers[0][1] == 0:
        farmers.pop(0)

    cost += farmers[0][0]
    farmers[0][1] -= 1

file_out.write(str(cost)+'\n')

