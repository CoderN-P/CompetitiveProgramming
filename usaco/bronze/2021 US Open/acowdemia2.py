k, n = list(map(int, input().split()))
members = input().split()
projects = [input().split() for _ in range(k)]

for member1 in members:
    res = ''
    for member2 in members:
        if member1 == member2:
            res += 'B'
            continue
        else:
            for project in projects:



    print(res)