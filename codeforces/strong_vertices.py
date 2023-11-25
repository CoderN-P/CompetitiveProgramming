t = int(input())


for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = sorted([(i+1, x[0]-x[1]) for i, x in enumerate(zip(a, b))], key=lambda x: x[1], reverse=True)

    s = [c[0][0]]
    for i in range(1, n):
        if c[i][1] == c[0][1]:
            s.append(c[i][0])


    print(len(s))
    print(' '.join(list(map(str, sorted(s)))))


