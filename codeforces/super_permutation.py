t = int(input())
res = []

# For odd numbers, no super permutation exists
# For even numbers, last modulo is (n)(n+1)/2 mod n = n/2
# For odd numbers, last modulo is (n)(n+1)/2 mod n = 0
# n=4, 4, 3, 2, 1
# 0, 3, 1, 2
# n = 3, 1, 2, 3
# 1, 0, 0
# n = 6, 6, 5, 4, 3, 2, 1
# 0, 5, 3, 0

for _ in range(0, t):
    n = int(input())
    if n%2 == 1:
        if n == 1:
            res.append('1')
        else:
            res.append('-1')
    else:
        ans = [n, n-1]
        ans += list(range(2, n-1))
        if 1 not in ans:
            ans.append(1)
        res.append(' '.join(map(str, ans)))
for i in res:
    print(i)