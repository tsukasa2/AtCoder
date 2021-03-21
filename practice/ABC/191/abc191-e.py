N, M = map( int, input().split() )
ABC = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b, c ) in ABC:
    a -= 1
    b -= 1
    connect[ a ].append( ( b, c ) )

from heapq import heappush, heappop
INF = 10 ** 8
ans = [ 10 ** 8 for _ in range( N ) ]
for start in range( N ):
    visited = [ False for _ in range( N ) ]
    cost = [ INF for _ in range( N ) ]
    queue = []
    for v, c in connect[ start ]:
        heappush( queue, ( c, v ) )
        cost[ v ] = c
    
    while queue:
        c, v = heappop( queue )
        visited[ v ] = True
        
        if v == start:
            ans[ start ] = c
            break

        for ( nv, nc ) in connect[ v ]:
            if visited[ nv ] == False:
                if cost[ nv ] > c + nc:
                    cost[ nv ] = c + nc
                    heappush( queue, ( c + nc, nv ) )

for i in range( N ):
    if ans[ i ] == INF:
        ans[ i ] = -1

print( "\n".join( map( str, ans ) ) )