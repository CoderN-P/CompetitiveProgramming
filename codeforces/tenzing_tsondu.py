t = int(input())

res = []

for _ in range(0, t):
    n, m = list(map(int, input().split()))

    a = sum(list(map(int, input().split())))
    b = sum(list(map(int, input().split())))

    if a > b:
        res.append('Tsondu')
    elif a < b:
        res.append('Tenzing')
    else:
        res.append('Draw')

for i in res:
    print(i)