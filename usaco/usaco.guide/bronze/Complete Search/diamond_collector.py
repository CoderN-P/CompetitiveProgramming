"""
ID: neel.pa1
LANG: PYTHON3
TASK: diamond
"""

fin = open('diamond.in', 'r')

N, K = map(int, fin.readline().split())

diamonds = []

for _ in range(N):
    diamonds.append(int(fin.readline()))

largest = 0
curlargest = 0
for x in range(N):
    for y in range(N):
        if diamonds[x] <= diamonds[y] <= diamonds[x] + K:
            curlargest += 1
    largest = max(largest, curlargest)
    curlargest = 0

print(largest, file=open('diamond.out', 'w'))
