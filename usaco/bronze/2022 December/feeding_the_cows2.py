"""
ID: neel.pa1
LANG: PYTHON3
"""

t = int(input())

for i in range(0, t):
    n, k = list(map(int, input().split()))
    s = input()
    if k == 0:
        print(s)
        continue
    new = ['.']*n
    coveredG = -1
    coveredH = -1
    for j in range(0, n):
        print(coveredH, coveredG)
        if coveredG < j:
            if j + k < n:
                new[j+k] = 'G'
                coveredG += j+k*2
                if j == 0:
                    coveredG += 1
            else:
                new[-1] = 'G'
                coveredG = n-1
        if coveredH < j:
            if j + k < n:
                new[j+k] = 'H'
                coveredH += j+k*2
                if j == 0:
                    coveredH += 1
            else:
                new[-1] = 'H'
                coveredH = n - 1

        if coveredG - k == j+k and coveredH < j:
            new[j+k-1] = 'H'
            coveredH += j+k*2 - 1
        if coveredH - k == j+k and coveredG < j:
            new[j + k - 1] = 'G'
            coveredG += j + k * 2 - 1

    print(''.join(new))


