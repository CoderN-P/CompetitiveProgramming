n = int(input())
h = list(map(int, input().split()))

prev, curr = 0,  abs(h[1] - h[0])

for i in range(2, n):
    prev, curr = curr, min(curr + abs(h[i]-h[i-1]), prev + abs(h[i]-h[i-2]))

print(curr)


