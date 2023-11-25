t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    frogs = sorted(list(map(int, input().split())))
    s = 0

    for i in range(frogs[0], n+1):
        cur = 0
        for frog in frogs:
            if frog > i:
                break
            if i%frog == 0:
                cur += 1
        s = max(s, cur)

    res.append(s)

for i in res:
    print(i)