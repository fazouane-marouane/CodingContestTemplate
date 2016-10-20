import collections
import sys

Graph = collections.namedtuple('Graph', ['nodes', 'edges'], verbose=False)

def Floyd(nodes, edges):
    dists = [[ 0 if x == y else 1 if (x, y) in edges else float('inf') for y in nodes] for x in nodes]
    for k in nodes:
        for i in nodes:
            for j in nodes:
                tmp = dists[i][k] + dists[k][j]
                if tmp < dists[i][j]:
                    dists[i][j] = tmp
    return dists

def ShortestPathsFactory(graph):
    dists = Floyd(*graph)
    return lambda N1, N2:(
        dists[N1][N2]
    )

def Main():
    graph = Graph(nodes= range(0, 10), edges = [(0, 1), (1, 2), (1, 3), (2, 3)])
    ShortestPaths = ShortestPathsFactory(graph)
    print(ShortestPaths(0, 1))
    print(ShortestPaths(0, 2))
    print(ShortestPaths(0, 3))
    print(ShortestPaths(1, 3))
    print(ShortestPaths(0, 4))

Main()
