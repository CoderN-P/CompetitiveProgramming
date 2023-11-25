'''
ID: neel.pa1
LANG: PYTHON3
TASK: lineup
'''

fin = open("lineup.in", "r")
fout = open("lineup.out", "w")

n = int(fin.readline())
nmap = sorted(['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue'])
graph = {i:[] for i in nmap}

for _ in range(0, n):
    v = fin.readline().split()
    a, b = v[0], v[-1]
    graph[a].append(b)
    graph[b].append(a)
result = []
for a, b in graph.items():
    if a not in result:
        if len(b) != 2:
            result.append(a)
        if len(b) == 1:
            result.append(b[0])
            b = graph[b[0]]
            while len(b) > 1:
                if b[0] in result:
                    result.append(b[1])
                    b = graph[b[1]]
                else:
                    result.append(b[0])
                    b = graph[b[0]]



for i in result:
    fout.write(i+'\n')



