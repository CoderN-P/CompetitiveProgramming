"""
ID: neel.pa1
LANG: PYTHON3
TASK: ride
"""
file_in = open("ride.in", "r")
file_out = open('ride.out', 'w')
l = [ord(a) - 96 for a in file_in.readline().strip().lower()]
l2 = [ord(a) - 96 for a in file_in.readline().strip().lower()]

n = 1
n2 = 1

for i in l2:
    n2 *= i

for i in l:
    n *= i

if n % 47 == n2 % 47:
    file_out.write("GO\n")

else:
    file_out.write("STAY\n")
