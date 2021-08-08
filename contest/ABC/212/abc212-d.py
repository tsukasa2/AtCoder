Q = int( input() )
query = [ list( map( int, input().split() ) ) for _ in range( Q ) ]

import heapq
queue = []
offset = 0
for q in query:
    if q[ 0 ] == 1:
        heapq.heappush( queue, q[ 1 ] - offset )
    elif q[ 0 ] == 2:
        offset += q[ 1 ]
    else:
        print( offset + heapq.heappop( queue ) )