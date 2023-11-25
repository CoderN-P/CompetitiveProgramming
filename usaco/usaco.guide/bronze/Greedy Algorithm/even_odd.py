n = int(input())
arr = list(map(int, input().split()))
odds = sum([1 for i in arr if i%2 == 1])
evens = sum([1 for i in arr if i%2 == 0])
# even + odd = odd
# even + even = even
# odd + odd = even

res = 0

if odds == 0 and evens == 0:
    res = 0
elif odds == 0:
    res = 1
else:
    if odds < evens:
        res = odds + 1
    else:
        res = evens*2
        v = odds-evens
        if v > 0:
            if v - (2*((v)//2)) != (v)//2 - 1:
                v = v-1
                if v - (2*((v)//2)) != (v)//2 - 1:
                    v = v-1

            res += (2*(v))//3

print(res)
