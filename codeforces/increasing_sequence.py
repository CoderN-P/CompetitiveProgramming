t = int(input())

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(range(1, n+1))

    while True:
        for i in range(0, n):
            if b[i] == a[i]:
                for j in range(i, n):
                    b[j] += 1

        for i in range(0, n):
            if a[i] == b[i]:
                break
        else:
            break

    print(b[-1])



