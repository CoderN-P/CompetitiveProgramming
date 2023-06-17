"""
ID: neel.pa1
LANG: PYTHON3
"""

t = int(input())

cases = []

for _ in range(t):
    n, k = list(map(int, input().split()))
    cases.append([n, k, input()])


for i, case in enumerate(cases):
    n, k, s = case
    if k == 0:
        print(n)
        if i == t-1:
            s = s+'\n'
        print(s)
    else:

        l = []
        r = []
        for i in range(0, n):
            if s[i] == 'G':
                z = [i]
            else:
                z = []
            for j in range(1, k+1):

                if i-j >= 0 and s[i-j] == 'G':
                    z.append(i-j)
                if i+j < n and s[i+j] == 'G':
                    z.append(i+j)
            l.append(z)
            if s[i] == 'H':
                z = [i]
            else:
                z = []
            for j in range(1, k + 1):
                if i - j >= 0 and s[i - j] == 'H':
                    z.append(i - j)
                if i + j < n and s[i + j] == 'H':
                    z.append(i + j)
            r.append(z)

        res = '.'*n
        c = 0

        g = []

        for i in range(0, n):
            if len(l[i]) > len(r[i]):
                g.append([l[i], 'G'])
            else:
                g.append([r[i], 'H'])





        print(g)
        if i == t-1:
            res = res+'\n'
        print(n-res.count('.'))
        print(res)


