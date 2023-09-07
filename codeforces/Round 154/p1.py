t = int(input())
res = []


def checkPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(0, t):
    n = list(input())
    for i in range(1, len(n)):
        v = int(n[0] + n[i])
        if checkPrime(v):
            res.append(v)

            break


for i in res:
    print(i)
