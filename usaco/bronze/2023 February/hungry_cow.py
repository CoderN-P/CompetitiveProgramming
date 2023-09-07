n, t = list(map(int, input().split()))

available = 0
res = 0
prev = 0
for i in range(0, n):
    print(available)
    d, b = list(map(int, input().split()))
    if available >= d-prev:
        res += d-prev
        available -= d - prev
        if available < 0:
            available = b
        else: available+=b
    else:
        res += available
        available = b
    prev = d


if prev != t:
    if available >= t-prev:
        res += t-prev
    else:
        res += available
else:
    res += 1

print(res)
