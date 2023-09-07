q = int(input())

ans = []
for _ in range(0, q):
    s = input()
    res = 0
    if len(s) > 3:
        res += len(s) - 3
        m = [0, 0]
        for i in range(0, len(s)-2):
            score = 0
            if s[i] == 'M':
                score += 1
            if s[i+1] == "O":
                score += 3
            if s[i+2] == "O":
                score += 1
            if score >= m[0]:
                m[0] = score
                m[1] = s[i]+s[i+1]+s[i+2]
        s = m[1]

    if len(s) < 3:
        ans.append(-1)

    else:
        if s[1] == "M":
            ans.append(-1)
        else:
            if s[0] == "O":
                res += 1
            if s[2] == "M":
                res += 1
            ans.append(res)


for i in ans:
    print(i)
