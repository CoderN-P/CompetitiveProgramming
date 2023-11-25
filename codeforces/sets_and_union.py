t = int(input())

for _ in range(0, t):
    n = int(input())
    sets = [set(list(map(int, input().split()))) for _ in range(0, n)]
    all = sets[0]
    for i in range(1, n):
        all = all.union(sets[i])

    s = None
    ans = 0
    for i in range(1, 51):
        for se in sets:
            if i not in se:
                if s:
                    s = s.union(se)
                else:
                    s = se
        if s:
            if len(s) < len(all):
                ans = max(ans, len(s))
                print(s)
        s = None
    print(all)
    print(ans)


