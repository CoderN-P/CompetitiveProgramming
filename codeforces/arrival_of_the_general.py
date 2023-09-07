n = int(input())

line = list(map(int, input().split()))

maxIndex = 0
maxHeight = 0
minIndex = len(line) - 1
minHeight = float('inf')

for i in range(0, len(line)):
    if line[i] > maxHeight:
        maxHeight = line[i]
        maxIndex = i
    if line[i] <= minHeight:
        minIndex = i
        minHeight = line[i]
ans = maxIndex + len(line)-1-minIndex
if maxIndex > minIndex:
    ans -= 1
print(ans)

