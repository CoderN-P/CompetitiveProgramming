n, d = list(map(int, input().split()))
l = list(map(int, list(input())))

lilies = [i for i in range(0, n) if l[i] == 1]

print(lilies)