t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    res.append(max(a[-1]*a[-2], a[0]*a[1]))

for i in res:
    print(i)