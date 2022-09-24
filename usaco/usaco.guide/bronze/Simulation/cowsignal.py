"""
ID: neel.pa1
LANG: PYTHON3
TASK: cowsignal"""

file_in = open('cowsignal.in', 'r')
file_out = open('cowsignal.out', 'w')

m, n, k = list(map(int, file_in.readline().split()))


converted = ''

for i in range(0, m):
    sig = file_in.readline().strip('\n')
    amplified = ''

    for char in sig:
        amplified += char*k
    amplified += '\n'
    amplified *= k
    converted += amplified

file_out.write(converted)