Q = int( input() )
Query = [ list( map( int, input().split() ) ) for _ in range( Q ) ]

from collections import deque
import heapq
sorted_A = []
add_to_A = deque( [] )
for querry in Query:
    if querry[ 0 ] == 1:
        add_to_A.append( querry[ 1 ] )
    elif querry[ 0 ] == 2:
        if sorted_A:
            x = heapq.heappop( sorted_A )
            print( x )
        else:
            print( add_to_A.popleft() )
    else:
        while add_to_A:
            x = add_to_A.popleft()
            heapq.heappush( sorted_A, x )