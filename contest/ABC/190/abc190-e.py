N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]
K = int( input() )
C = list( map( int, input().split() ) )

from collections import deque

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = AB[ i ]
    graph[a].append(b)
    graph[b].append(a)

def BFS( s, g ):
    dist = [-1] * (N+1)
    dist[0] = 0
    dist[s] = 0

    d = deque()
    d.append(s)

    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    return dist[ g ]

import itertools

cost = [ [ 0 for _ in range( K ) ] for _ in range( K ) ]
for i in range( K ):
    for j in range( K ):
        cost[ i ][ j ] = BFS( i + 1, j + 1 )

l = [ i for i in range( 1, K + 1 ) ]
ans = 10 ** 18
for p in itertools.permutations( l, K ):
    cost_i = 0
    for i in range( K - 1 ):
        cost_i += cost[ p[ i ] - 1 ][ p[ i + 1 ] - 1 ]
    ans = min( ans, cost_i )

print( max( ans + 1, -1 ) )