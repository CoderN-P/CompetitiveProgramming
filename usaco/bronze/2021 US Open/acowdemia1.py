"""
ID: neel.pa1
LANG: PYTHON3
TASK: acowdemia1
"""

n, l = list(map(int, input().split()))
papers = sorted(list(map(int, input().split())), reverse=True)


def calcHIDX():
    h = 0
    for i in range(0, n):
        if papers[i] >= i+1:
            h += 1
        else:
            break
    return h

v = calcHIDX()

if v == n:
    print(v)
elif papers[v] < v:
    print(v)
else:
    print(v+1 if l > v else v)








