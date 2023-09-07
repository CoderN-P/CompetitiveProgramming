t = int(input())

ans = []
for _ in range(0, t):
    a, b, c = list(map(int, input().split()))

    if a+b >= 10 or a+c>=10 or c+b>=10:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)
