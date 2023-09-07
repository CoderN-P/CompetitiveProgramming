n, q = list(map(int, input().split()))
a = input().split()

n1 = a.count('1')
n0 = a.count('0')
for _ in range(0, q):
    query, k = input().split()

    if query == '2':
        if int(k) <= n1:
            print(1)
        else:
            print(0)
    else:
        k = int(k)
        if a[k-1] == '1':
            a[k-1] = '0'
            n1 -= 1
            n0 += 1
        else:
            a[k-1] = '1'
            n1 += 1
            n0 -= 1

