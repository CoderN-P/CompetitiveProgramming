t = int(input())

res = []

for _ in range(0, t):
    n, c = list(map(int, input().split()))
    paintings = list(map(int, input().split()))

    a = 4*n
    b = sum(list(map(lambda x: 4*x, paintings)))
    c1 = sum(list(map(lambda x: x**2, paintings))) - c

    ans = (-b + (b**2 - (4*a*c1))**0.5)/(2*a)

    res.append(ans)

for i in res:
    print(int(i))




