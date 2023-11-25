'''
ID: neel.pa1
LANG: PYTHON3
TASK: sprime
'''

fin = open("sprime.in", "r")
fout = open("sprime.out", "w")
numDigits = int(fin.readline())

def checkPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True


def recur(n, digitsAdd):
    if digitsAdd == 0:
        fout.writelines(str(n)+'\n')
        print('added', n)
        return
    n *= 10
    if checkPrime(n + 1):
        recur(n + 1, digitsAdd - 1)
    if checkPrime(n + 3):
        recur(n + 3, digitsAdd - 1)
    if checkPrime(n + 7):
        recur(n + 7, digitsAdd - 1)
    if checkPrime(n + 9):
        recur(n + 9, digitsAdd - 1)


recur(2, numDigits-1)
recur(3, numDigits-1)
recur(5, numDigits-1)
recur(7, numDigits-1)

