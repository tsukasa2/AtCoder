N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N ) ]
for a, b in AB:
    connect[ a - 1 ].append( b - 1 )

dim = [ 0 ] * N
for u in range( N ):
    for v in connect[ u ]:
        dim[ v ] += 1

ans = []

import heapq
visited = [ False ] * N
queue = []
for v in range( N ):
    if dim[ v ] == 0:
        heapq.heappush( queue, v )

while queue:
    v = heapq.heappop( queue )
    visited[ v ] = True
    for u in connect[ v ]:
        if visited[ u ] == False:
            dim[ u ] -= 1
            if dim[ u ] == 0:
                heapq.heappush( queue, u )

    ans.append( v + 1 )

if False in visited:
    print( -1 )
else:
    print( *ans, sep = " " )