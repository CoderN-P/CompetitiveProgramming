n = input()

res = 0
for i in range(0, len(n)):
    if int(n[i-1]+n[i])%4 == 0:
        res += 1

        if i > 0:
            if (10*int(n[i-1]) + int(n[i]))%4 == 0:
                res += i

print(res)





