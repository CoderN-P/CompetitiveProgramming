'''
ID: neel.pa1
LANG: PYTHON3
TASK: pprime
'''

fin = open("pprime.in", "r")
fout = open("pprime.out", "w")
a, b1 = list(map(int, fin.readline().split()))


def checkPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def createPalindrome(inp, b, isOdd):
    n = inp
    palin = inp

    if isOdd:
        n = n // b

    while n > 0:
        palin = palin * b + (n % b)
        n = n // b
    return palin


res = []
for j in range(1, 3):
    i = 1
    while createPalindrome(i, 10, j % 2) <= b1:
        v = createPalindrome(i, 10, j % 2)
        if v >= a:
            if checkPrime(v):
                res.append(v)
        i = i + 1

res.sort()

for i in res:
    fout.write(str(i)+'\n')
