t = int(input())
res = []

for _ in range(0, t):
    s = input()
    pi = '3141592653589793238462643383279'
    ans = 0
    for i in range(0, len(s)):
        if s[i] != pi[i]:
            break
        ans += 1

    res.append(ans)

for i in res:
    print(i)