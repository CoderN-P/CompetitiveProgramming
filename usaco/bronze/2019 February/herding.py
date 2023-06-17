"""
ID: neel.pa1
LANG: PYTHON3
TASK: herding
"""

import sys

sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')
a, b, c = map(int, input().split())

# Best scenario: the three elements are already in order.
if c == a + 2:
    print(0)

elif b == a + 2 or c == b + 2:
    print(1)

else:
    print(2)
"""
The worst case is incrementing by 1 in the largest gap.
3 5 9 -> 5 6 9 -> 6 7 9 -> 7 8 9
"""
print(max(b - a, c - b) - 1)
