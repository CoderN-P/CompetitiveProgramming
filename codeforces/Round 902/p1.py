t = int(input())

for _ in range(0, t):
    n = int(input())
    efficiencies = list(map(int, input().split()))
    sum_known_efficiencies = sum(efficiencies)
    print(-sum_known_efficiencies)