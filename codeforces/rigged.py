t = int(input())

for _ in range(0, t):
    n = int(input())
    athletes = [list(map(int, input().split())) for _ in range(0, n)]
    poly = athletes.pop(0)

    for i in athletes:
        if i[0] >= poly[0] and i[1] >= poly[1]:
            print(-1)
            break
    else:
        print(poly[0])
