t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    odd = ((n-4)*2 + 9)//2 + 1
    s = odd**2 - 25
    v = 1 if n > 4 else 0
    res.append(26+(v)*s)

for i in res:
    print(i)