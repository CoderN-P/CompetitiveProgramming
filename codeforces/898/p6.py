t = int(input())

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    fruits = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    l = list(range(0, n))
    s = []
    for i in range(0, n-1):
        s.append(i)

        if heights[i]%heights[i+1] != 0:
            for j in s:
                l[j] = i
            s = []

        else:
            if i == n-2:
                for j in s:
                    l[j] = i+1

    ps = [fruits[0]]
    for i in range(1, n):
        ps.append(fruits[i]+ps[i-1])

    m_size = 0

    lo, hi = 0, n-1

    while lo < hi:
        mid = (lo+hi)//2

        



