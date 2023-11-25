'''
ID: neel.pa1
LANG: PYTHON3
TASK: cownomics
'''

fin = open('cownomics.in', 'r')
fout = open('cownomics.out', 'w')

n, m = list(map(int, fin.readline().split()))
spotty = [fin.readline() for _ in range(0, n)]
plain = [fin.readline() for _ in range(0, n)]

ans = 0
for sec1 in range(0, m):
    for sec2 in range(sec1+1, m):
        for sec3 in range(sec2+1, m):
            cset = []
            sset = []

            for cow in range(0, n):
                sset.append(spotty[cow][sec1]+spotty[cow][sec2]+spotty[cow][sec3])
                cset.append(plain[cow][sec1]+plain[cow][sec2]+plain[cow][sec3])

            if not any(i in cset for i in sset):
                ans += 1

fout.write(str(ans))


