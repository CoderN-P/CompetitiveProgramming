'''
ID: neel.pa1
LANG: PYTHON3
TASK: planting
'''

fin = open("planting.in", "r")
fout = open("planting.out", "w")

n = int(fin.readline())
graph = {}

for _ in range(n-1):
    a, b = fin.readline().split()
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

fout.write(str(max(len(b)+1 for a, b in graph.items())))


