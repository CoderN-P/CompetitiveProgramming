t = int(input())

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == 1:
        print('NO')
        continue

    ones = a.count(1)
    if sum(a) < ones+n:
        print('NO')
    else:
        print('YES')


