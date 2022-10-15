"""
ID: neel.pa1
LANG: PYTHON3
TASK: crypt1
"""

file_in = open('crypt1.in', 'r')
file_out = open('crypt1.out', 'w')
n = int(file_in.readline())
digits = list(map(int, file_in.readline().split()))
result = 0


def valid(j, i):
    validity = []
    if all([int(char) in digits for char in str(j)]):
        validity.append(True)

    if all([int(char) in digits for char in str(i)]):
        validity.append(True)

    if all([int(char) in digits for char in str(j * int(str(i)[0]))]) and len(str(j * int(str(i)[0]))) == 3:
        validity.append(True)

    if all([int(char) in digits for char in str(j * int(str(i)[1]))]) and len(str(j * int(str(i)[1]))) == 3:
        validity.append(True)

    if all([int(char) in digits for char in str(j * i)]) and len(str(j*i)) == 4:
        validity.append(True)

    return 1 if len(validity)==5 else 0


for j in range(100, 1001):
    for i in range(10, 100):
        result += valid(j, i)

file_out.write(str(result)+'\n')
