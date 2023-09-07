t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    s = input()
    start = s[0]
    result = start
    skip = False
    for i in range(1, n):
        if skip:
            skip = False
            continue
        character = s[i]
        if character == start:
            if i < n-1:
                start = s[i+1]
                result += start
                skip = True
    res.append(result)

for i in res:
    print(i)
