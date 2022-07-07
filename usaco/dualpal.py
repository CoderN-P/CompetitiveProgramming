"""
ID: neel.pa1
LANG: PYTHON3
TASK: dualpal
"""

n, s = list(map(int, open('dualpal.in', 'r').readline().split()))
out = open('dualpal.out', 'w')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def convert(base, input):
    mods = []
    while input > 0:
        mods.append(numbers[input % base])
        input //= base
    mods.reverse()
    return ''.join(mods)


num = s + 1

results = []
while num > s:
    if len(results) == n:
        break

    vals = []
    for b in range(2, 11):
        v = convert(b, num)

        if v == v[::-1]:
            vals.append(b)

    if len(vals) > 1:
        results.append(str(num) + '\n')

    num += 1

out.write(''.join(results))
