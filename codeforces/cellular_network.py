n, m = list(map(int, input().split()))

cities = list(map(int, input().split()))
towers = list(set(list(map(int, input().split()))))
m = len(towers)
i, j = 0, 0
res = 0
print(towers)
while i < n:
    city = cities[i]
    tower = towers[j]

    res = max(res, abs(city-tower))

    if city > tower:
        i += 1
    else:
        if i < n -1:
            i += 1

print(res)
