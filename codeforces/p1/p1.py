t = int(input())

res = []

for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    evens = []
    ei = []
    odds = []
    oi = []
    for i, el in enumerate(arr):
        if el%2 == 0:
            evens.append(el)
            ei.append(i)
        else:
            odds.append(el)
            oi.append(i)

    evens = sorted(evens)
    ei = sorted(ei)
    odds = sorted(odds)
    oi = sorted(oi)
    result = [0 for _ in range(n)]
    for i in range(0, len(evens)):
        result[ei[i]] = evens[i]
    for i in range(0, len(odds)):
        result[oi[i]] = odds[i]

    if result == sorted(arr):
        res.append('YES')
    else:
        res.append("NO")

for i in res:
    print(i)
