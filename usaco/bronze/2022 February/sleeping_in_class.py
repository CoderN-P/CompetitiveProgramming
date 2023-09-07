t = int(input())
ans = []

from math import sqrt


def factors(n1, ma):
    step = 2 if n1 % 2 else 1
    mi = float('inf')
    for i in range(1, int(sqrt(n1)) + 1, step):
        if n1 % i == 0:
            o = n1 // i
            if i < ma <= o:
                mi = min(mi, o)
                continue
            if i >= ma:
                return i
    return mi


for _ in range(0, t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = max(a)
    v = sum(a)
    f = factors(v, m)
    if f == float('inf'):
        f = 0

    res = 0
    temp = 0
    rtemp = 0
    for i in range(0, n):
        if temp == 0 and a[i] == f:
            continue
        temp += a[i]
        rtemp += 1
        if temp == f:
            res += rtemp-1
            temp = 0
            rtemp = 0

    ans.append(res)

for i in ans:
    print(i)

