t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    x = list(map(int, input().split()))
    total = 0
    for i in x:
        total += min(a, i)
        if i >= a:
            total -= 1

    print(total + b)