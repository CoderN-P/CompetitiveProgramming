"""
ID: neel.pa1
LANG: PYTHON3
TASK: palsquare
"""

base = int(open("palsquare.in", "r").readline().strip())
out = open("palsquare.out", "w")

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def convert(base, input):
    mods = []
    while input > 0:
        mods.append(numbers[input % base])
        input //= base
    mods.reverse()
    return ''.join(mods)

palsquares = []
for n in range(1, 301):
    converted_square = convert(base, n**2)
    if converted_square == converted_square[::-1]:
        converted = convert(base, n)
        palsquares.append(f'{converted} {converted_square}\n')

out.write(''.join(palsquares))


