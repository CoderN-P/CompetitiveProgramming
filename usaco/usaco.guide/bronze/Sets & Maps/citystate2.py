fin = open("citystate.in", "r")
fout = open("citystate.out", "w")

n = int(fin.readline())

cs = [fin.readline().split() for _ in range(0, n)]

res = 0

for i in range(0, n):
    for j in range(i+1, n):
        if cs[i][0][:2] == cs[j][1] and cs[i][1] == cs[j][0][:2]:
            res += 1

print(res)