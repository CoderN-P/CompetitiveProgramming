def solve():
    n = int(input())
    p = list(map(int, input().split()))
    res = 0
    p_inv = {p[i]:i for i in range(0, n)}
    for i in range(0, n):
       if p[i] < n and i > p_inv[p[i]+1]:
            res += 1
    return res

t = int(input())
res = [solve() for _ in range(0, t)]
for i in res:
    print(i)