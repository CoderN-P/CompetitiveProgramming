t = int(input())

res = []

for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    odds = len([i for i in arr if i%2==1])
    evens = len([i for i in arr if i%2==0])


    if odds%2 == 0:
        res.append('YES')
    else:
        res.append('NO')


for i in res:
    print(i)