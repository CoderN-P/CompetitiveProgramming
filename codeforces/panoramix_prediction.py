n, m = list(map(int, input().split()))


def checkPrime(i):
    if i == 1:
        return False
    for l in range(2, int(i / 2) + 1):
        if i % l == 0:
            return False
    return True


if not checkPrime(n):
    print('NO')
else:
    s = n + 1
    while True:
        if checkPrime(s):
            break
        s += 1

    if s == m:
        print('YES')
    else:
        print('NO')
