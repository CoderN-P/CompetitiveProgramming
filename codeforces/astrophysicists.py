t = int(input())

for _ in range(0, t):
    n, k, g = list(map(int, input().split()))
    print(g*k//n, g*k%n)