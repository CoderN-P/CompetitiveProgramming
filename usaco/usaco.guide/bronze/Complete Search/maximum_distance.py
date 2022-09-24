"""
This algorithm needs to be run through PyPi to succeed
"""
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


result = 0
for i in range(n):
    for j in range(i+1, n):
        result = max(result, ((x[i] - x[j])**2 + (y[i] - y[j])**2))

print(result)

