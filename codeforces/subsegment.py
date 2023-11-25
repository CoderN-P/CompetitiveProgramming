t = int(input())

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    a = list(map(int,input().split()))
    if k in a:
        print('YES')
    else:
        print('NO')
'''
    for startIdx in range(0, n-1):
        if ans == 'YES':
            break
        for endIx in range(startIdx+1, n):
            c = a[startIdx:endIx+1]
            m = 0
            km = 0
            for i in c:
                if i == k:
                    km = c.count(i)
                else:
                    m = max(m, c.count(i))
            print(c, km, m)
            if km > m:
                ans = 'YES'
                break

    print(ans)
    '''

