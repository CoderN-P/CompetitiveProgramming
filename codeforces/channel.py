t = int(input())

res = []

for _ in range(0, t):
    n, a, q = list(map(int, input().split()))
    notifications = input()
    read = list(range(1, a+1))
    online = list(range(1, a+1))
    offline = list(range(a+1, n+1))
    maybe = 0
    for i in range(0, q):
        n1 = notifications[i]
        if n1 == '-':
            offline.append(online.pop())
        else:
            v = offline.pop()
            if v in read:
                maybe += 1
            else:
                read.append(v)
            online.append(v)

    if len(read) == n:
        res.append('YES')
    elif len(read) + maybe >= n:
        res.append('MAYBE')
    else:
        res.append('NO')

for i in res:
    print(i)


