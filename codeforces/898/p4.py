t = int(input())

for _ in range(0, t):
    n, k = list(map(int, input().split()))
    s = input()
    ans = 0
    cur = 0
    for i in range(0, n):
        if s[i] == 'B':
            cur += 1
        elif cur > 0:
            cur += 1
        if cur == k:
            ans += 1
            cur = 0
        if i == n-1 and cur > 0:
            ans += 1
    print(ans)