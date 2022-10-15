"""
ID: neel.pa1
LANG: PYTHON3
"""

n = int(input())
p = list(map(int, input().split()))

result = n

for i in range(0, n):
    for j in range(i+1, n):
        avg = sum(p[i:j+1])/(j-i+1)
        if avg in p[i:j+1]:

            result += 1
print(result)