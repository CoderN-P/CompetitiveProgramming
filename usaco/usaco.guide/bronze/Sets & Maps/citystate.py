"""
ID: neel.pa1
LANG: PYTHON3
TASK: citystate
"""
from collections import defaultdict

pairs = []
with open("citystate.in") as read:
    for _ in range(int(read.readline())):
        city, state = read.readline().strip().split()
        city = city[:2]  # We only care about the first two letters of the city
        pairs.append((city, state))

seen = defaultdict(int)
total = 0
for c, s in pairs:
    if c != s:
        total += seen[s + c]
    seen[c + s] += 1

print(total, file=open("citystate.out", "w"))

