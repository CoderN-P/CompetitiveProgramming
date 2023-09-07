n = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)
s = sum(coins)
cs = 0
c = 0

for i in range(0, n):
    if cs > s - cs:
        break
    else:
        c += 1
        cs += coins[i]

print(c)
