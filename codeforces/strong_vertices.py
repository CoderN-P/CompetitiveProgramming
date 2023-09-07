t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = ''
    c = 0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if (a[i]-a[j]) < (b[i]-b[j]):
                break
        else:
            ans += str(i+1)
            c += 1
            if i < n -1:
                ans += ' '

    res.append((ans, c))

for i in res:
    print(str(i[1]))
    print(i[0])

