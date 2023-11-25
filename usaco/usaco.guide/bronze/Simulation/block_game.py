fin, fout = open('blocks.in', 'r'), open('blocks.out', 'w')
n = int(fin.readline())
blocks = [fin.readline().split() for _ in range(0, n)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = [0 for _ in range(26)]


for i in range(0, n):
    s1 = blocks[i][0]
    s2 = blocks[i][1]
    for i in range(0, 26):
        letter = alphabet[i]
        ans[i] += max(s1.count(letter), s2.count(letter))

for i in ans:
    fout.write(str(i)+'\n')