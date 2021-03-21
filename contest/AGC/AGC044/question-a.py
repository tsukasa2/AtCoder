t = int( input() )
nabcd = []
for _ in range( t ):
    n, a, b, c, d = map( int, input().split() )
    nabcd.append( [ n, a, b, c, d ] )

def adj( k, a_i, b_i, c_i, d_i ):
    if k > 0:
        return [ ( a_i, 2*k ), ( b_i, 3*k ), ( c_i, 5*k ), ( d_i, k+1 ), ( d_i, k-1 ) ]
    elif k == 0:
        return [ ( d_i, k+1 ) ]
    else:
        return []

import heapq
def search( goal, a_i, b_i, c_i, d_i ):
    INF = 10 ** 20
    VISITED = 1
    NOT_VISITED = 0
    NODE = 2 * goal # 諸
    cost = [ INF ] * ( NODE+1 )
    cost[ 0 ] = 0
    visit = [ NOT_VISITED ] * ( NODE+1 )
    queue = [ ( cost[ 0 ], 0 ) ]
    while visit[ goal ] == NOT_VISITED:
        _, v = heapq.heappop( queue )
        visit[ v ] = VISITED
        for cost_vu, u in adj( v, a_i, b_i, c_i, d_i ):
            if u > NODE:
                continue
            if visit[ u ] == VISITED:
                continue
            if cost[u] > cost[v] + cost_vu:
                cost[u] = cost[v] + cost_vu
                heapq.heappush( queue, ( cost[u], u ) )
    print( cost[ goal ] )

for i in range( t ):
    search( nabcd[i][0], nabcd[i][1], nabcd[i][2], nabcd[i][3], nabcd[i][4] )