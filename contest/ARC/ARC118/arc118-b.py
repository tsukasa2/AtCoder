K, N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

B = [ 0 for _ in range( K ) ]

import heapq
queue = []

rest = M
for i in range( K ):
    B[ i ] = A[ i ] * M // N
    rest -= B[ i ]

for i in range( K ):
    heapq.heappush( queue, ( N * B[ i ] - M * A[ i ], i ) )

for _ in range( rest ):
    _, i = heapq.heappop( queue )
    B[ i ] += 1
    heapq.heappush( queue, ( N * B[ i ] - M * A[ i ], i ) )

print( " ".join( map( str, B ) ) )