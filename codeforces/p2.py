t = int(input())
res = []
minSum = float('inf')

def cost(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for _ in range(0, t):
    n, k, a, b = list(map(int, input().split()))
    cities = [list(map(int, input().split())) for _ in range(n)]
    sv = cost(cities[a-1], cities[b-1])
    graph = []

    for i in range(0, n):
        l = []
        for j in range(0, n):
            if i == j:
                continue
            if i < k and j < k:
                l.append([j, 0])
            else:
                v = cost(cities[i], cities[j])
                if v < sv or (i == a-1 and j == b-1) or (i==b-1 and j==a-1):
                    l.append([j, v])
        graph.append(l)

    minSum = float('inf')

    def getMinPathSum(graph, vis, src, dest, currSum):
        global minSum
        if (src == dest):
            minSum = min(minSum, currSum)
            return
        else:
            vis[src] = True
            for node in graph[src]:
                if not vis[node[0]]:
                    vis[node[0]] = True
                    getMinPathSum(graph, vis,  node[0], dest, currSum + node[1])
                    vis[node[0]] = False

            vis[src] = False


    getMinPathSum(graph, [False for _ in range(0, n)], a - 1, b - 1, 0)
    res.append(minSum)

for i in res:
    print(i)


