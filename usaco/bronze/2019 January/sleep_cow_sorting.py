fin = open('sleepy.in')
fout = open('sleepy.out')

n = int(fin.readline())
arr = list(map(int, fin.readline().split()))
sort = sorted(arr)
# Use binary search

lo, hi = 0, n

while lo < hi:
    mid = (lo+hi)//2
    # Determine if [mid] moves is enough
