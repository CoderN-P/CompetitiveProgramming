import math

t = int(input())

for _ in range(0, t):
    n, m = list(map(int, input().split()))
    x = input()
    s = input()
    if s in x:
        print(0)
        continue
    for i in range(1, 8):
        if len(x) >= 25:
            print(-1)
            break
        x = x+x
        if s in x:
            print(i)
            break




