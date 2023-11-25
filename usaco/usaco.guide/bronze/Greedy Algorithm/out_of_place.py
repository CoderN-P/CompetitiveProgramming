fin = open('outofplace.in', 'r')
fout = open('outofplace.out', 'w')
n = int(fin.readline())
a = [int(fin.readline()) for _ in range(0, n)]

# find bessie
b_h = 0
b_i = 0
pair_count = 0
move_idx = 0
for i in range(1, n):

    if a[i] < a[i-1]:
        b_h = a[i]
        b_i = i
        break

for i in range(0, n):
    if b_h < a[i]:
        move_idx = i
        break

for i in range(0, n):
    if i < move_idx:
        continue
    if i >= b_i:
        break

    if a[i] == a[i-1]:
        pair_count = 1

fout.write(str(b_i-move_idx-pair_count))