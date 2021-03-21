N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

import heapq
A_heap = [ - a for a in A ]
heapq.heapify( A_heap )

for _ in range( M ):
    X = heapq.heappop( A_heap )
    heapq.heappush( A_heap, - ( - X // 2 ) )

print( - sum( A_heap ) )