"""
ID: neel.pa1
LANG: PYTHON3
TASK: lifeguards
"""
with open("lifeguards.in") as read:
    n = int(read.readline())
    lifeguards = []
    for _ in range(n):
        lifeguards.append([int(i) for i in read.readline().split()])

# Max time we'll have to process up to
max_time = max(max(l) for l in lifeguards)

max_cover = 0
"""
Simulate firing each lifeguard and compute the total
time covered by the remaining lifeguards
"""
for i in range(n):
    time_covered = 0
    for t in range(1, max_time + 1):
        # Try to find a cow that can cover this interval
        for j in range(n):
            # Check that it's not the fired cow
            if j != i:
                if lifeguards[j][0] <= t < lifeguards[j][1]:
                    # One more time slot covered- no need to search further
                    time_covered += 1
                    break
    max_cover = max(time_covered, max_cover)

print(max_cover, file=open("lifeguards.out", "w"))
