"""
ID: neel.pa1
LANG: PYTHON3
TASK: billboard
"""

file_in = open("billboard.in", "r")
file_out = open("billboard.out", "w")
n1 = list(map(int, file_in.readline().split()))
n2 = list(map(int, file_in.readline().split()))
n3 = list(map(int, file_in.readline().split()))


def overlap_area(a, a2):
    if (a[3] <= a2[1]) or (a[1] >= a2[3]):
        return (a[2] - a[0]) * (a[3] - a[1])

    if (a[0] >= a2[2]) or (a[2] <= a2[0]):
        return (a[2] - a[0]) * (a[3] - a[1])

    return ((a[2] - a[0]) * (a[3] - a[1])) - (
                (min(a[2], a2[2]) - max(a[0], a2[0])) * (min(a[3], a2[3]) - max(a[1], a2[1])))


file_out.write(str(overlap_area(n1, n3) + overlap_area(n2, n3)) + '\n')
