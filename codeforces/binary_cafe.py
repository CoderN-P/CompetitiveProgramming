import math
t = int(input())
res = []

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    if n < k:
        affordable = math.floor(math.log2(n))+1
    else:
        affordable = math.log2(k)



for i in res:
    print(i)

