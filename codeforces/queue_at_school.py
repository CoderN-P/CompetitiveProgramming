n, t = list(map(int, input().split()))
s = list(input())
frozen = []
for _ in range(0, t):
    for i in range(0, n-1):
        if s[i] == 'B' and s[i+1] == 'G' and i not in frozen:
            s[i] = 'G'
            s[i+1] = 'B'
            frozen.append(i+1)
    frozen = []

print(''.join(s))
