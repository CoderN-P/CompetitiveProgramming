'''
ID: neel.pa1
LANG: PYTHON3
TASK: factory
'''

fin = open('factory.in', 'r')
fout = open('factory.out', 'w')

n = int(fin.readline())

graph = {}

for _ in range(n - 1):
    a, b = list(map(int, fin.readline().split()))
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]


def recur(station, target):
    if station not in graph:
        return False
    else:
        v = graph[station]
        if target in v:
            return True
        else:
            for s in v:
                if recur(s, target):
                    return True
            return False


for station, access in graph.items():
    for i in range(1, n + 1):
        if i == station or i in access:
            continue
        if not recur(station, i):
            break
    else:
        fout.write(str(station))
        break
else:
    fout.write('-1')
