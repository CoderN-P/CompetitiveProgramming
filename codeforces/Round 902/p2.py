
t = int(input())

for _ in range(0, t):
    n, p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cost = 0
    residents = [0 for _ in range(0, n)]
    sharers = [(a[i], b[i], i) for i in range(0, n)]
    sharers.sort(key=lambda x: x[0]/x[1], reverse=True)

    print(sharers)

    while sharers:
        s = sharers.pop(-1)

        if s[1] < p:
            t = 0

            print(s)

            for i in range(0, len(sharers)):
                if residents[sharers[i][2]] == 0 and t < s[0]:
                    residents[sharers[i][2]] = 1
                    t += 1

                else:
                    break
            cost += s[1] * t

        if residents[s[2]] == 0:
            residents[s[2]] = 1
            cost += p

    print(cost)
