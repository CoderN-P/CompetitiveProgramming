"""
ID: neel.pa1
LANG: PYTHON3
TASK: blist
"""

fin = open("blist.in", "r")

max_time = 1000
event = [0 for i in range(max_time + 1)]

n = int(fin.readline().strip())

for i in range(n):
    start, end, amt = map(int, fin.readline().strip().split())

    # at time start, cow i needs to be milked, so
    # we'll need amt additional buckets (hence adding amt)
    event[start] += amt

    # at time end, cow i is done milking, so we can free up
    # amt buckets (hence subtracting amt)
    event[end] -= amt
"""
res represents the maximum number of buckets we'll need 
to use at any given time and cur represents 
how many buckets we need to use at the current 
time we're processing
"""
res = 0
cur = 0

for i in range(max_time + 1):
    # at time i, the number of buckets in use changes by event[i]
    # so we want to update the number of buckets
    # we are currently using accordingly
    cur += event[i]

    # we want res to be the greatest number of buckets
    # we need to use at any given point in time
    res = max(res, cur)

print(res, file=open('blist.out', 'w'))
